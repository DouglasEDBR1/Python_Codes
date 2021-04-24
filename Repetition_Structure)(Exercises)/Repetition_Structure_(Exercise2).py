#1. Ler 5 notas e informar a média
#Com while


numero = 1
soma = 0
while numero <= 5:
  nota = float(input('Digite a nota:'))
  soma += nota
  numero += 1
print(f'A média é', soma / 5)