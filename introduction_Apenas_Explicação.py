
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
Cada pessoa possuirá no 'Par B'  ( 60000000 * 1000000)/2  pares de bases de DNA.

"""

"""

Se você tem um arquivo de texto com 60000000 vezes 1000000 caracteres, teríamos um total de 60 bilhões de caracteres.
Vamos supor que cada caractere ocupe 1 byte (8 bits) em seu arquivo de texto. Portanto, o tamanho total em bytes seria igual a 60 bilhões de bytes.
Para converter bytes em gigabytes, usamos a seguinte fórmula:
Tamanho em gigabytes = Tamanho em bytes / (1024 * 1024 * 1024)
Aplicando essa fórmula ao tamanho em bytes que obtivemos, temos:
Tamanho em gigabytes = 60 bilhões de bytes / (1024 * 1024 * 1024)
Agora, vamos calcular:
60 bilhões de bytes ≈ 55.9 gigabytes (GB)
Portanto, 60000000 vezes 1000000 caracteres em um arquivo de texto ocupariam aproximadamente 55.9 gigabytes (GB).

"""
