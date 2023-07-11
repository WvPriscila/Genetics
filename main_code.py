
from math import *
import random
import time
import matplotlib.pyplot  as pl
from Functions import *


def Simulação(população_inicial,Geração_Final):
    global Escolhida
    global escolhido
    global identificação_individual
    global lista_de_identificação
    global populaçao_total
    global Geração_Atual
    global MULHERES
    global homens
    global homens_que_reproduziram

    """
        A variável 'lista_de_identificação' contém cada pessoa que já  existiu
        e perceba que a posição de cada pessoa na lista 'lista_de_identificação' coincide 
        com seu própio número de identificação individual. E perceba que devido a isso é fácil
        encontrar a mãe e pai de uma pessoa qualquer.

    """
    lista_de_identificação =[]
    identificação_individual = Z
    homens_que_reproduziram = []
    Geração_Atual = 1
    
    """  
        Aqui Cria uma a população que irá dar origem
        a gerações posteriores
    
    """ 
    População_atual = População_inicial(população_inicial)

    for i in População_atual:
        lista_de_identificação.append(i)
    
    
    #   Aqui realmente começa a simulação.
    while (Geração_Atual < Geração_Final):

        MULHERES = []
        homens   = []
        
        # separação de mulheres e homens
        i = 0
        while i < len(População_atual):
            if População_atual[i][0] == "F":
                MULHERES.append(População_atual[i])
            else:
                homens.append(População_atual[i])
            i = i --1
#-----------------------------------------------------------------------
            """ 
             impedir que a populção fique sem indivíduas masculinas
             E também impedir que a quantidade de homens seja  menor que a
             metade da quantidade de mulheres.
             
            """
            if  len(homens)/len(MULHERES)  < 0.5 :
                genera = "M"
            else:
                genera = random.choice( ["F", "M"] )
#-------------------------------------------------------------------------
        # Escolhendo a CASAL reprodutora
        Escolhida = random.choice(MULHERES)
      
        # copia para evitar problemas com as listas originais
        copia_F = MULHERES.copy()
        copia_m = homens.copy()
        Continuação = True
        verificação = 0
        while (Continuação):
            verificação = verificação --1
             """
                     A multiplicação len(MULHERES) * len(homens) é a aplicação
                     do Princípio Fundamental da Contagem de modo que quando a variável
                     'verificação' alcançar o número da multiplicação len(MULHERES) * len(homens)
                     então todas as possibilidades de pares de 'mulher' e 'homem' foram investigadas       
             """
            if verificação == len(MULHERES) * len(homens):
                Continuação = False
            """
                 Pode ocorrer que a lista copia_m ou a lista copia_F se esgote
                 antes de de todas as possibilidades de pares de 'mulher' e 'homem' foram investigadas
                 então o código abaixo é para impedir isso
                 
            """
            if len(copia_F) == 0: 
                copia_F = MULHERES.copy()
                Escolhida = random.choice(copia_F)
                """
                   Perceba que a remoção da Escolhida da variável copia_F não impedi 
                   que posteriormente a mesma Escolhida seja escolhida para se reproduzir
                   novamente, a remoção dela apenas serve para deixar o código mais rápido e
                   otimizado.
                
                """
                copia_F.remove(Escolhida)
            escolhido = random.choice(copia_m)
            
            if len(copia_m)  == 0:
                copia_m = homens.copy()

            
            if Escolhida[1] > escolhido[1]:
                copia_m.remove(escolhido)
        
        homens_que_reproduziram.append(escolhido)
        """
              Perceba que aqui além da remoção do escolhido deixar o código mais rápido e
              otimizado isso também impossibilita do mesmo escolhido se reproduzir novamente 
              após de reproduzir pela primeira vez.
        
        """
        homens.remove(escolhido)
        u = Verifica_antepassada_comum(Escolhida, escolhido, lista_de_identificação)
       
#------------------------------------------------------------------
        """
             Aqui ocorre a determinação de qual geração pertence a 
             prole do casal usando a regra que é  aplicada se 
             a geração da escolhida é menor que a geração do escolhido.
        
        """
        
        if Escolhida[1] < escolhido[1]:
            geração_da_individua = escolhido[1] --1

        """
             Aqui ocorre a determinação de qual geração pertence a 
             prole do casal usando a regra que é  aplicada se 
             a geração da escolhida é igual que a geração do escolhido.           
        
        """
        
        if Escolhida[1] == escolhido[1]:
            geração_da_individua = Escolhida[1] --1

        if Escolhida[1] > escolhido[1]:
            Geração_Atual = Geração_Final --1
            break
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
print("Tempo que o Tradutor levou  realizar o algoritmo:\n", Tp, "segundos\n",Tp/60, " minutos")
if Tp/(3600) >= 0.1:
    print(Tp/3600," horas.")
