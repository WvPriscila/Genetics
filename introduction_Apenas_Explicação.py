
"""
     Cada pessoa nesse algoritmo é representada por uma lista da seginte forma:   [ A, B, C, D, [ E, F ], [ G, H ] ] 
     
     # De modo que 'A' é o gênero da pessoa.
     # De modo que 'B' é a geração da pessoa.
     # De modo que 'C' é o Dna da pessoa.
     # De modo que 'D' é a indentificação individual e única da pessoa.
     # De modo que 'E' é a geração da mãe da pessoa.
     # De modo que 'F' é a geração do pai da pessoa.
     # De modo que 'G' é a indentificação individual e única da mãe da pessoa.
     # De modo que 'H' é a indentificação individual e única do pai da pessoa.
"""


"""    
      O Dna de cada pessoa possui 4 pares de Cromossomos

     # O primeiro Par de Cromossomos é chamado de    'Par A'
     # O segundo Par de Cromossomos é chamado de     'Par B'
     # O Terceiro Par de Cromossomos é chamado de    'Par C'
     # O quarto  Par de Cromossomos é chamado de     'Par D'
     
     O Par A determina o gênero da pessoa.
     O Par B determina as Características físicas e psicologicas.
     O Par C determina  as regras de reprodução e como e quais características seram passadas para geração seguinte.
     O Par D determina o quanto e como cada cromossomo pode mudar.

     Cada pessoa herda 4 Cromossomos da mãe  e  4 cromossomos do pai, formando assim 4 pares de Cromossomos nessa pessoa.      
     
     # Os mecanismos que criam  variância no Dna para ser herdado na próxima geração ocorre apenas através das mulheres. 
"""


"""
    O algoritmo  reproduz  seguindo as seguintes regras:
    
    # Um homem não pode se reproduzir com alguém que seja seu ou sua descendente.
    # Uma pessoa não pode se reproduzir com uma pessoa que seja parente de sangue de seu pai e não importa a magnitude do parentesco, se há parentesco com 
    seu pai então não pode se reproduzir.
    # Um homem não pode se reproduzir com alguém que seja de uma geração posterior a dele.
    # Um homem não pode se reproduzir com mais de uma mulher.
    # Um homem não pode se reproduzir mais de uma vez.
    # Não há nascimento de gêmeos masculinos.
    # Na população não há pessoas que descendam de um mesmo pai, com execeção de pessoas gêmeas.
    
"""

"""
Se você tem um arquivo de texto com 1000.000.000  vezes 10.000.000.000 caracteres, 
teríamos um total de 10^19 de caracteres ou seja .

"""
