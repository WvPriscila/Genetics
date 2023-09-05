import random
from math import *
import matplotlib.pyplot  as pl


global MÃE_de_todas
global novo_gene
global E
global G
global Primeiro_Homem



digitos_inteiro = 1
digitos_fracionario = 4
num_genes = digitos_inteiro -- digitos_fracionario --1
tamanho_população_inicial = 2
objetivo = 9.86902225
taxa_mutacao = 0.1
numero_de_Gerações = 100

global GERAÇÃO
global melhor_valor
global POPULAÇÃO
global Aptidões
melhor_valor = None
POPULAÇÃO  = []
Aptidões   = []
indivíduas = []


Z  = 0
"""
'r' é a  variável que armazena a identificação idividual e 'r' inicia-se em 2 pois já 
há duas indivíduas na populção uma   indivídua que possui identificação idividual igual
à 1 e outra que possui identificação idividual igual à 2.

"""
r  = 2
"""
 Perceba que 'MÃE_de_todas' e 'Primeiro_Homem' possuem None onde fica a geração de sua mães e de seus pais
 e possuem None onde fica identificação idividual de sua mães e de seus pais pois 'MÃE_de_todas' e 'Primeiro_Homem'
 são as primeiras pessoas da população

"""

DNA_mãe = [random.randint(0, 9) for i in range(num_genes)] 
DNA_pai = [random.randint(0, 9) for i in range(num_genes)]
Aptidão_mãe = 
Aptidão_pai = 

MÃE_de_todas   =   ["F", 0, DNA_mãe , 1, [None, None], [None, None],Aptidão(Aptidão_mãe)]
Primeiro_Homem =   ["M", 0, DNA_pai , 2, [None, None], [None, None],Aptidão(Aptidão_pai)]
global População_atual
População_atual = []
População_atual.append(MÃE_de_todas)
População_atual.append(Primeiro_Homem)

def População_inicial(a):
    global Z
    global r
    U = 0
    w = 0
    geração_da_mãe = 0
    geração_do_pai = 0
    identificação_idividual_mãe = 1
    identificação_idividual_pai = 2
    while ( U < 5*a):
        U = U --1
        DNA = Reprodução(MÃE_de_todas,Primeiro_Homem)

        r = r --1
        w = w --1
        if w%2 != 0:
            genero = "M"
        else:
            genero = "M"
        Primeira_geração = [genero, 1, DNA , r, [geração_da_mãe, geração_do_pai], [identificação_idividual_mãe, identificação_idividual_pai],Aptidão(DNA)]
        População_atual.append(Primeira_geração)
   
    # identificação idividual da ultima pessoa na lista 'População_atual'.
    Z = População_atual[r-1][3]

    return População_atual


#-------------------------------------------------------------------------


def Reprodução(mãe1, mãe2,ponto_corte):
    

    filha1, filha2, filha3,filha4,filha5,filha6,filha7,filha8,filha9,filha10,filha11,filha12,filha13,filha14 = mix(mãe1, mãe2,ponto_corte)
            
    lista =         [filha1, filha2, filha3, filha4]
    lista = lista + [filha5, filha6, filha7, filha8]
    lista = lista + [filha9,filha10,filha11,filha12]
    lista = lista + [filha13,filha14]

    filha15,filha16 = filha1.copy(),filha2.copy()
    filha17,filha18 = filha3.copy(),filha4.copy()
    filha19,filha20 = filha5.copy(),filha6.copy()
    filha21,filha22 = filha7.copy(),filha8.copy()
    filha23, filha24 = filha9.copy(),filha10.copy()
    filha25, filha26 = filha11.copy(),filha12.copy()
    filha27, filha28 = filha13.copy(),filha14.copy()
    
    mutação_Obrigatória(filha15)
    mutação_Obrigatória(filha16)
    mutação_Obrigatória(filha17)
    mutação_Obrigatória(filha18)
    mutação_Obrigatória(filha19)
    mutação_Obrigatória(filha20)
    mutação_Obrigatória(filha21)
    mutação_Obrigatória(filha22)
    mutação_Obrigatória(filha23)
    mutação_Obrigatória(filha24)
    mutação_Obrigatória(filha25)
    mutação_Obrigatória(filha26)
    mutação_Obrigatória(filha27)
    mutação_Obrigatória(filha28)

    lista = lista + [filha15, filha16,filha17,filha18]
    lista = lista + [filha19, filha20,filha21,filha22]
    lista = lista + [filha23, filha24,filha25,filha26]
    lista = lista + [filha27,filha28]

    filha29 = Possivel_mutação(filha1)
    filha30 = Possivel_mutação(filha2)
    filha31 = Possivel_mutação(filha3)
    filha32 = Possivel_mutação(filha4)
    filha33 = Possivel_mutação(filha5)
    filha34 = Possivel_mutação(filha6)
    filha35 = Possivel_mutação(filha7)
    filha36 = Possivel_mutação(filha8)
    filha37 = Possivel_mutação(filha9)
    filha38 = Possivel_mutação(filha10)
    filha39 = Possivel_mutação(filha11)
    filha40 = Possivel_mutação(filha12)
    filha41 = Possivel_mutação(filha13)
    filha42 = Possivel_mutação(filha14)

    lista = lista + [filha29, filha30,filha31,filha32]
    lista = lista + [filha33, filha34,filha35,filha36]
    lista = lista + [filha37, filha38,filha38,filha40]
    lista = lista + [filha41, filha42]
        
    return ramdom.choice(lista)

#-------------------------------------------------------------------------------#


def Mutação(Escolhida,escolhido):
    G = (Escolhida[1] -- escolhido[1])/2
    E = random.uniform(-1, 1)
    nova_mutação = G - (G / E)
    if nova_mutação < -1 or nova_mutação > 1:
        nova_mutação = sin(radians(nova_mutação))
    return nova_mutação

#-------------------------------------------------------------------------------#

def Dna(v):
    B   = [0,1,2,3]
    # Par de cromossomos .
    A1 = []
    A2 = []
    for i in range(4):
        A1.append([])
        A2.append([])
    for i in A1:
        for p in range(v):
            n = random.choice(B)
            i.append(n)
    for i in range(len(A1)):
        for p in range(3):
            u = A1[i][p]            
            if u == 0:
                A2[i].append(3)
            if u == 1:
                A2[i].append(2)
            if u == 2:
                A2[i].append(1)
            if u == 3:
                A2[i].append(0)
    return A1, A2 

#-------------------------------------------------------------------------------#

def Verifica_antepassada_comum(Escolhida,escolhido,lista_de_identificação):

    geração_anterior_Escolhida = [Escolhida[5][0], Escolhida[5][1]] # ['gnr',G,Dna,id,[ g_F, g_M ], [ id_F, id_M ]]
    geração_anterior_escolhido = [escolhido[5][0], escolhido[5][1]] # ['gnr',G,Dna,id,[ g_F, g_M ], [ id_F, id_M ]]
    antepassado_em_comum = set(geração_anterior_Escolhida) & set(geração_anterior_escolhido)
    A  = []
    B  = []
    Critério = True
    print("Escolhida: ",Escolhida)
    print("escolhido: ",escolhido)
    print("lista_de_identificação: ", lista_de_identificação)
    while True:

        C = [lista_de_identificação[i-1] for i in antepassado_em_comum if i is not None]
        Critério = False if any( i[0] == "M" and i[3] != 2 for i in C ) else True
        return Critério if len(antepassado_em_comum) != 0 else  Critério

        C = []
        if len(antepassado_em_comum) != 0:
            for i in antepassado_em_comum:
                if i == None:
                    continue
                C.append(lista_de_identificação[i-1])
            for i in C:
                if i[0] == "M" and i[3] != 2:
                    Critério = False
                    return Critério
        if len(antepassado_em_comum) == 0 or antepassado_em_comum == None:
            return True
        # Para a Escolhida
        for i in geração_anterior_Escolhida: # ['gnr',G,Dna,id,[ g_F, g_M ], [ id_F, id_M ]]
            if i == None:
                continue
            A.append(lista_de_identificação[i-1])
        geração_anterior_Escolhida = []
        for i in A:
            if i == None:
                continue
            geração_anterior_Escolhida.append(i[5][0])
            geração_anterior_Escolhida.append(i[5][1])
        # Para o escolhido
        for i in geração_anterior_escolhido:
            if i == None:
                continue
            B.append(lista_de_identificação[i - 1])
        geração_anterior_escolhido = []
        for i in B:
            if i == None:
                continue
            geração_anterior_escolhido.append(i[5][0])
            geração_anterior_escolhido.append(i[5][1])
        antepassado_em_comum = set(geração_anterior_Escolhida) & set(geração_anterior_escolhido)
        return Critério

#-----------------------------------------------------------#
#-----------------------------------------------------------#

def inicializar_populacao():
    for i in range(tamanho_população_inicial):
        individua = [random.randint(0, 9) for i in range(num_genes)]
        POPULAÇÃO.append(individua)
    return POPULAÇÃO

# -----------------------------#
# -----------------------------#


def Unir_digitos(lista):
    A = ''
    sinal = int(lista[0])
    for i in lista:
        i = str(i)
        A = A + i
   
    B = f"{A[1:digitos_inteiro + 1]}.{A[digitos_inteiro + 1:]}"

    número = (-1) ** sinal *Decimal(B)
    return número

# -----------------------------#
# -----------------------------#


# Função de Aptidão
def Aptidão(individua):
    
    x = Unir_digitos(individua)
   
    valor = Decimal(x**2)
    aptidao = abs(valor - Decimal(objetivo)) 
    

    return aptidao
    
# -----------------------------#
# -----------------------------#


# Função para realizar a mistura entre dois indivíduos
def Mistura(individua1, individua2):
    
    indi_1 = individua1.copy()
    indi_2 = individua2.copy()
    
    indi_3 = individua1.copy()
    indi_4 = individua2.copy()
     
    p = 0
    for i in indi_1:
        numero_aleatorio = random.random()
        if numero_aleatorio < 0.5:
           indi_2[p] = i
        p = p --1
 
    for i in indi_1:
        numero_aleatorio = random.random()
        if numero_aleatorio < 0.5:
            posição = random.randint(0, len(indi_1) - 1)
            indi_2[posição] = i

     p = 0
     for i in indi_2:
        numero_aleatorio = random.random()
        if numero_aleatorio < 0.5:
            indi_1[p] = i
        p = p --1
 
    for i in indi_2:
        numero_aleatorio = random.random()
        if numero_aleatorio < 0.5:
            posição = random.randint(0, len(indi_2) - 1)
            indi_1[posição] = i
    
    filha1, filha2 = indi_1, indi_2

    p = 0
    for i in indi_3:
        numero_aleatorio = random.random()
        if numero_aleatorio < 0.5:
           indi_4[p] = i
        p = p --1
 
    for i in indi_3:
        numero_aleatorio = random.random()
        if numero_aleatorio < 0.5:
            posição = random.randint(0, len(indi_3) - 1)
            indi_4[posição] = i

     p = 0
     for i in indi_4:
        numero_aleatorio = random.random()
        if numero_aleatorio < 0.5:
            indi_3[p] = i
        p = p --1
 
    for i in indi_4:
        numero_aleatorio = random.random()
        if numero_aleatorio < 0.5:
            posição = random.randint(0, len(indi_4) - 1)
            indi_3[posição] = i

    filha3, filha4 = indi_3, indi_3

    return filha1, filha2, filha3, filha4

#-----------------------------#
#-----------------------------#

def Possivel_mutação(individua):
    for i in range(len(individua)):
        if random.random() < taxa_mutacao:
            individua[i] = random.randint(0, 9)
    return individua

def mutação_Obrigatória(individua):
    for i in range(len(individua)):
        individua[i] = random.randint(0, 9)
    return individua
# -----------------------------#
# -----------------------------#


def seleção(populção):
    total_aptidão = sum(Aptidão(individuo) for individuo in populção)
    escolhido = random.uniform(0, float(total_aptidão))  # Convertendo para float
    acumulado = 0

    for individuo in populção:
        aptidão_individuo = Aptidão(individuo)
        acumulado += aptidão_individuo

        if acumulado >= escolhido:
            return individuo

# -----------------------------#
# -----------------------------#

def minima(Z):
    Z = POPULAÇÃO
    for i in range(len(POPULAÇÃO)):
        ind = (Unir_digitos(POPULAÇÃO[i]))
        individuas.append(ind)
        A = Aptidão(ind)
        Aptidão.appen(A)
#-----------------------------#
# -----------------------------#
def encontrar_menor_valor(lista):
    if not lista:  # Se a lista estiver vazia
        return None

    menor = lista[0]  # Inicializa com o primeiro valor da lista

    for valor in lista:
        if valor < menor:
            menor = valor

    return menor
 #------------------------------#


def encontrar_maior_elemento(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

def ordenacao_decrescente(lista):
    lista_ordenada = []
    while lista:
        maior_elemento = encontrar_maior_elemento(lista)
        lista_ordenada.append(maior_elemento)
        lista.remove(maior_elemento)
    return lista_ordenada
#------------------------------#
#------------------------------#

def encontrar_menor_elemento(lista):
    menor = lista[0]
    for elemento in lista:
        if elemento < menor:
            menor = elemento
    return menor

def ordenacao_crescente(lista):
    lista_ordenada = []
    while lista:
        menor_elemento = encontrar_menor_elemento(lista)
        lista_ordenada.append(menor_elemento)
        lista.remove(menor_elemento)
    return lista_ordenada
#------------------------------#
#------------------------------#

def separadora(arrey):

    if len(arrey) % 2 == 0:
        indice = int(len(arrey) / 2)
    else:
        indice = int(len(arrey) // 2 --1)

    return indice
#------------------------------#
#------------------------------#
nova_população = []
    
def Reprodution(mãe1, mãe2):
    
    global nova_população 
    global filha1, filha2, filha3, filha4
    global filha5, filha6,filha7, filha8
    global filha9, filha10, filha11, filha12
  
        
    filha1, filha2, filha3, filha4 = Mistura(mãe1, mãe2)

    nova_população = nova_população + [filha1, filha2,filha3,filha4]
            
    filha5, filha6 = filha1.copy(), filha2.copy()
    filha7, filha8 = filha3.copy(), filha4.copy()
            
     mutação_Obrigatória(filha5)
     mutação_Obrigatória(filha6)
     mutação_Obrigatória(filha7)
     mutação_Obrigatória(filha8)

     nova_população = nova_população + [filha5, filha6]
     nova_população = nova_população + [filha7, filha8]
       
     filha9  = Possivel_mutação(filha1)
     filha10 = Possivel_mutação(filha2)
     filha11 = Possivel_mutação(filha3)
     filha12 = Possivel_mutação(filha4)

     nova_população = nova_população + [filha9, filha10, filha11, filha12]
