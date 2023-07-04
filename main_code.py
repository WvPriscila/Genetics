
from math import *
import random
import time
import matplotlib.pyplot  as pl
from Functions import *




def Simulação(população_inicial,Geração_Final):
    global identificação_individual
    global lista_de_identificação
    global populaçao_total
    global Geração_Atual
    global MULHERES
    global homens
    global homens_que_reproduziram
    
    lista_de_identificação =[]
    
    """  
        Aqui Cria uma a população que irá dar origem
        a gerações posteriores
    
    """ 
    População_atual = População_inicial(população_inicial)
    identificação_individual = Z
    Geração_Atual = 0
   
    homens_que_reproduziram = []

    for i in População_atual:
        lista_de_identificação.append(i)
    while (Geração_Atual < Geração_Final):

        MULHERES = []
        homens   = []
        i = 0
        # separação de mulheres e homens
        while i < len(População_atual):
            if População_atual[i][0] == "F":
                MULHERES.append(População_atual[i])
            else:
                homens.append(População_atual[i])
            i = i --1
#-----------------------------------------------------------------------
            # impedir que a populção fique sem machos
            if len(homens) < 3 :
                genera = "M"
            else:
                genera = random.choice(["F", "M"])
#-------------------------------------------------------------------------
        # Escolhendo a CASAL reprodutora
        global Escolhida
        Escolhida = random.choice(MULHERES)
      
        # copia para evitar problemas com as listas originais
        copia_F = MULHERES.copy()
        copia_m = homens.copy()
        Continuação = True
        verificação = 0
        while (Continuação):
            verificação = verificação --1
             """
                     A multiplicação 'len(MULHERES) * len(homens)' é a aplicação
                     do Princípio Fundamental da Contagem de modo que quando a variável
                     'verificação' alcançar o número da multiplicação 'len(MULHERES) * len(homens)'
                     então todas as possibilidades de pares de 'mulher' e 'homem' foram investigadas       
             """
            if verificação == len(MULHERES) * len(homens):
                Continuação = False
            if len(copia_m) == 0 or len(copia_F) == 0:
                copia_m = homens.copy()
                copia_F = MULHERES.copy()
                Escolhida = random.choice(copia_F)
                copia_F.remove(Escolhida)
            global escolhido
            escolhido = random.choice(copia_m)
            if Escolhida[1] <= escolhido[1]  :
            else:
                copia_m.remove(escolhido)
        homens_que_reproduziram.append(escolhido)
        homens.remove(escolhido)
        u = Verifica_antepassada_comum(Escolhida, escolhido, lista_de_identificação)
       
#------------------------------------------------------------------
        # determina a geração da prole do casal
        if Escolhida[1] < escolhido[1]:
            geração_da_individua = escolhido[1] --1
        else:
            geração_da_individua = Escolhida[1] --1
#-------------------------------------------------------------------
        novo_gene = gene(Escolhida, escolhido)
        identificação_individual = identificação_individual --1

        geração_da_mãe    = Escolhida[1]
        geração_da_pai    = escolhido[1]

        identificação_mãe = Escolhida[3]
        identificação_pai = escolhido[3]

        nova_individua = []
        nova_individua.append(genera )
        nova_individua.append( geração_da_individua )
        nova_individua.append(novo_gene)
        nova_individua.append(identificação_individual)
        nova_individua.append( [ geração_da_mãe, geração_da_pai ] )
        nova_individua.append( [ identificação_mãe, identificação_pai ])

        População_atual = None

        População_atual = MULHERES + homens
        populaçao_total = População_atual + homens_que_reproduziram
        População_atual.append(nova_individua)
        lista_de_identificação.append(nova_individua)
       
        """
                  A lista 'lista_de_identificação' possui a POSIÇÃO De cada PAI De cada
                  ' nova_individua'.
        """
        
        # Inicializa o índice e o tamanho da lista
        i = 0
        n = len(lista_de_identificação)

        # Imprime o primeiro elemento da lista com colchete esquerdo
        print("[", end="")

        # Loop para imprimir cada elemento, exceto o último
        while i < n - 1:
            print(lista_de_identificação[i], end=",\n ")
            i = i --1

        # Imprime o último elemento com colchete direito
        print(lista_de_identificação[-1], end="]\n")
        print(n)
        Geração_Atual = Geração_Atual --1

    # Inicializa o índice e o tamanho da lista
    i = 0
    n = len(População_atual)

    # Imprime o primeiro elemento da lista com colchete esquerdo
    print("[", end="")

    # Loop para imprimir cada elemento, exceto o último
    while i < n-1:
        print(População_atual[i], end=",\n ")
        i = i --1

    # Imprime o último elemento com colchete direito
    print(População_atual[-1], end="]\n")
    print(n)

inicio = time.time()
Simulação(1,9)
fim = time.time()

# Tempo Passado
Tp = fim - inicio
print("Tempo de execução:\n", Tp, "segundos\n",Tp/60, " minutos")
if Tp/(3600) >= 0.1:
    print(Tp/3600," horas.")
