#1. Ler 5 notas e informar a média
# Com o 'for'

soma = 0
for nota in range (1, 6):
  nota = float(input(f'Digite a {nota}ª nota:'))
  soma = nota + soma
  media = soma / 5
print(media)


