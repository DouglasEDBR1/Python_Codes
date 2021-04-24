#Leia a idade do usuário e classifique-o em:
#- Criança – 0 a 12 anos
#- Adolescente – 13 a 17 anos
#- Adulto – acima de 18 anos
#-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida


idade = int(input('Digite sua idade:'))
if idade >=0 and idade <=12:
  print('Criança')
elif idade >=13 and idade <=17:
  print('Adolescente')
elif idade < 0:
  print('idade inválida!')
else:
  print('Maior de 18 anos')

