import random
from math import *
import matplotlib.pyplot  as pl



"""
O DNA é como um livro de receitas que está dentro do nosso corpo.
Esse livro contém todas as informações sobre como nosso corpo deve
ser construído e como funcionam nossas características, como cor dos olhos, tipo de cabelo, etc.

Às vezes, quando o nosso corpo está fazendo cópias desse livro de receitas, podem ocorrer pequenos erros
chamados mutações. Esses erros são como letras que são escritas erradas em uma palavra no livro.

No caso dos seres humanos, estudos sugerem que esses erros acontecem aproximadamente a cada 100 a 300 milhões de
"letras" do nosso livro de receitas a cada geração. Isso significa que, em cada geração, algumas das informações
podem mudar um pouquinho por causa dessas mutações.

Essas mudanças são naturais e fazem parte  das espécies. Na maioria das vezes, elas não causam grandes 
problemas e não são percebidas. Às vezes, porém, essas mutações podem levar a diferenças nas características das 
pessoas, como uma altura um pouco diferente ou alguma habilidade especial.

Portanto, as mutações cromossômicas são como pequenos erros que acontecem quando nosso corpo faz cópias do nosso livro de receitas,
o DNA. Esses erros acontecem muito raramente, a cada 100 a 300 milhões de "letras" do DNA, mas são parte natural  da espécie.

No genoma humano, as mulheres têm dois cromossomos de gênero 'X', enquanto os homens têm um cromossomo 'X' e um cromossomo 'Y' . O cromossomo 'Y' é 
consideravelmente menor em tamanho em comparação com o cromossomo 'X' e contém menos pares de bases de DNA.

Em média, o cromossomo 'Y' humano contém cerca de 59 milhões de pares de bases, enquanto o cromossomo 'X' humano contém cerca de 155 milhões
de pares de bases. Isso significa que as mulheres têm, em média, um  mais de pares de bases de DNA do que os homens.


A maioria das informações genéticas importantes para a função e o desenvolvimento ocorre nos cromossomos  'autossomos', que são 
semelhantes entre homens e mulheres. É importante ressaltar que, apesar da diferença no tamanho dos cromossomos de gênero, ambos os  gêneroa 
humanos compartilham a maioria do genoma, com variações adicionais concentradas principalmente nos cromossomos de gênero.

então espara-se poder dizer que a taxa média de mutação de  pares de bases em relação a quantidade total de  pares de bases
é aproximadamente 300/3155 algo próximo de 9.5% de uma geração para a outra.

então se simularmos um cromossomo de 1000  pares de bases haveria uma mutação de aproximadamente 95 pares de bases em média.

"""
global MÃE_de_todas
global novo_gene
global E
global G
global Primeiro_Homem

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
MÃE_de_todas   =   ["F", 0, random.uniform(-1, 1), 1, [None, None], [None, None]]
Primeiro_Homem =   ["M", 0, random.uniform(-1, 1), 2, [None, None], [None, None]]
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
        GENE = gene(MÃE_de_todas,Primeiro_Homem)

        r = r --1
        w = w --1
        if w%2 != 0:
            genero = "M"
        else:
            genero = "M"
        Primeira_geração = [genero, 1, GENE, r, [geração_da_mãe, geração_do_pai], [identificação_idividual_mãe, identificação_idividual_pai]]
        População_atual.append(Primeira_geração)
   
    # identificação idividual da ultima pessoa na lista 'População_atual'.
    Z = População_atual[r-1][3]

    return População_atual

#-------------------------------------------------------------------------------#

def Mutação(Escolhida,escolhido):
    G = (Escolhida[1] -- escolhido[1])/2
    E = random.uniform(-1, 1)
    nova_mutação = G - (G / E)
    if nova_mutação < -1 or nova_mutação > 1:
        nova_mutação = sin(radians(nova_mutação))
    return nova_mutação

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



