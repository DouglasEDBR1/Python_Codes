#Variáveis STRINS(Manipulação)

a = 'casaco'
print(a)

#MAIÚSCULO

maiuscula = a.upper()
print(maiuscula)

#MINUSCULO
minuscula = a.lower()
print(minuscula)

#Primeira letra maiúscula (FUNÇÂO capalize)

capital = a.capitalize()
print(capital)

#Metade da palavra

metade_da_palavra = a  [0:3]
print(metade_da_palavra)

#Exemplo2

metade_da_palavra = a  [0:4]
print(metade_da_palavra)

#Ultimas Palavras

ultimas_letras = a[3:]  #3 útmas letras
print(ultimas_letras)

#Substituíção de caracteres (REPLACE) -> Utilizada para substituir as strings

b = a.replace('aco', 'inha') #varíavel 'b' recebe variável 'a'
print(a)
print(b)

c = a.replace('o' , 'a')
print(a)
print(c)

#PROCURAR CARACTÉRES - > (FIND) retorna a posição(índice) que a letra foi encontrada
c.find('s')

#Tamanho da String - > (LEN) Retorna a quantidade de índices
e = ' casaco '
print(len(e))

#Função STRIP - > Retira espaços antes e depois

f = e.strip()
print(len(f))