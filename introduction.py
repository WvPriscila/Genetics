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



"""
     Cada pessoa nesse algoritmo é representada da seginte forma:   [ A, B, C, D, [ E, F ], [ G, H ] ] 
     
     # De modo que 'A' é o gênero da pessoa
     # De modo que 'B' é a geração da pessoa
     # De modo que 'C' é o Dna da pessoa
     # De modo que 'D' é a indentificação individual e única da pessoa
     # De modo que 'E' é a geração da mãe da pessoa
     # De modo que 'F' é a geração do pai da pessoa
     # De modo que 'G' é a indentificação individual e única da mãe da pessoa
     # De modo que 'H' é a indentificação individual e única do pai da pessoa

"""

"""    
      O Dna de cada pessoa possui 3 pares de Cromossomos

     # O primeiro Par de Cromossomos é chamado de 'Par A'
     # O segundo Par de Cromossomos é chamado de 'Par B'
     # O Terceiro Par de Cromossomos é chamado de 'Par C'

     O Par A determina o gênero da pessoa
     O Par B determina as Características físicas e psicologicas
     O Par C determina determina as regras de reprodução e como e quais características seram passadas para geração seguinte

     Cada pessoa herda 3 Cromossomos da mãe  e  3 cromossomos do pai formando assim 3 pares de Cromossomos
      
"""


"""
    O algoritmo  reproduz  seguindo as seguintes regras:

    
    # Um homem não pode se reproduzir com alguém que seja seu ou sua descendente
    # Uma pessoa não pode se reproduzir com uma pessoa que seja parente de sangue de seu pai
    # Um homem não pode se reproduzir com alguém que seja de uma geração posterior a dele
    # Um homem não pode se reproduzir com mais de uma mulher
    # Um homem não pode se reproduzir mais de uma vez
    # Não há nascimento de gêmeos masculinos 
    
"""
