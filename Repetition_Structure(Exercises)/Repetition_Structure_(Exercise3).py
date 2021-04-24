#Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)
#Com o for



multiplicar = 1
for multiplicar in range (1, 11):
  numero = 3
  multiplicar = numero * multiplicar
  print(multiplicar)

print('*=' * 5)
print('Formatado')
print('*=' * 5)

for i in range (1, 11):
  print('3 x {} = {}'.format(i, 3 * i))