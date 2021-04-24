#Criar Um sistema com menu, utilizando estrutura de dados com fila e fila encadeada, que pegue o dados
#dos clientes e armazene em um arquivo txt.

#O Sistema se baseia na idéia de uma fila por ficha eletrônica, após chamar a ficha é efetuado
#um cadastro...



import random
import string
from time import sleep


def linha (tam = 40):
    return '=' * 40

def inicio (txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def menu (lista):
    inicio ('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print (f'{c} - {item}')
        c +=1
    print (linha())
    opcao = tratativa_de_erro ('Opção:')
    return opcao

def tratativa_de_erro (txt):
    while True:
        try:
            n1 = int(input(txt))
        except(ValueError, TypeError):
            print('Digite uma opção válida!')
            continue
        else:
            return n1


def insere(elemento,vfila):
    aux = {len(vfila):elemento}
    vfila.update(aux)


def imprime(vfila,tipo):
    if not fila_vazia(vfila):
        if tipo == 'P':
            print('PRÓXIMO - FICHA:', vfila[0])
        else:
            indice = len(vfila) - 1
            print(vfila[indice])
    else:
        print('A FILA ESTA VAZIA!')

def imprimeElemento(vfila, indice):
    print(f'PRÓXIMO: {vfila[indice]}')
    print('=&=' * 10)


def fila_vazia(vfila):
    if len(vfila) > 0:
        return False
    else:
        return True

def remove (vfila):
    aux = vfila[0]
    for i in range(0, len(vfila) -1):
        vfila[i] = vfila[i + 1]
    vfila.pop(len(vfila) - 1)
    return aux

def reordenarLista(vlista):
    total = len(vlista)

    if total > 1:

        for i in range(0, total - 1):
            vlista[i]['PROXIMO'] = i + 1


def insereElemento(vlista, cliente):
    indice = len(vlista)

    elemento = {'CLIENTE': cliente, 'PROXIMO': None}
    aux = {indice: elemento}
    vlista.update(aux)

    reordenarLista(vlista)

def fila_vazia2(vLista):
	if len(vLista) > 0:
		return False
	else:
		return True

def removeElemento(vLista, indice):
    org = {}
    for x in range(0, len(vLista)):
        if x != indice:
            org[x] = vLista[x]['CLIENTE']
        else:
            vLista.pop(indice)
    vLista.clear()
    for x in org.keys():
       insereElemento(vLista, org[x])



def criar_arquivo(nome):
    c = open (nome, 'wt+')
    c.close()

def verificar_arquivo(nome):
    try:
        n = open(nome, 'rt')
        n.close()
    except FileNotFoundError:
        return False
    else:
        return True


arquivo = 'cadastro_de_clientes.txt'
if not verificar_arquivo(arquivo):
    criar_arquivo(arquivo)

fila = {}
fila_prioridade = {}
cadastro = {}


ficha = random.sample(range(5, 50), 5)
for i in ficha:
    insere(i, fila)

letras = string.ascii_uppercase
for ficha_preferencial in range(0, 3):
    codigo = ''.join(random.choice(letras) for _ in range(3))

    insereElemento(fila_prioridade, codigo)

gerador = 0
while len(set(str(gerador))) != 6:
    gerador = random.randint(100000, 999999)


inicio ('Sistema de Cadastro')


while True:
    print(f'FILA: {fila}')
    print(f'FILA PRIORIDADE:{fila_prioridade}')
    op = menu (['Cadastrar Cliente', 'Chamar Ficha', 'Cadastrar Prioridade', 'Chamar Ficha Prioridade', 'Verificar Clientes'])

    if op == 1:
        if len(fila) < 1:
            inicio ('Não existe mais ficha no sistema!')
            sleep(2)
            continue
        else:
            inicio('Novo Cadastro')
            nome = str(input('Nome do Cliente:'))

            while True:
                cpf = input('CPF:')
                if len(cpf) == 11:
                    if cpf.isnumeric():
                        break
                print('Digite um número válido!')

            rua = input('RUA:')
            n1 = int(input('NÚMERO:'))
            while True:
                cep = input('CEP:')
                if len(cep) == 8:
                    if cep.isnumeric():
                        break
                print('CEP inválido!')
            cidade = str(input('Cidade:'))
            estado = str(input('Estado:'))
            inicio('GERANDO NÚMERO')
            print('processando...')
            sleep(3)
            inicio('Número do cliente gerado com sucesso!')
            numero = (f'(82){999}{gerador}')
            numero_novo = numero
            print(numero_novo)

        aux = [f'Nome: {nome} - Cpf: {cpf} - Rua: {rua} - Número: {n1} - cep: {cep} - Número Gerado {numero_novo}']

        insereElemento(cadastro, aux)

        print(len(cadastro)-1, cadastro[len(cadastro) -1])
        o = open(arquivo, 'at')
        o.write(f'{aux}\n')
        o.close()

        remove(fila)
        sleep(4)
    elif op == 2:

        inicio('Fila')
        imprime(fila, 'P')
        sleep(2)
    elif op == 3:
        if len(fila_prioridade) < 1:
            inicio('Não existe mais ficha no sistema!')
            sleep(2)
            continue
        else:
            print(f'FILA PRIORIDADE:{fila_prioridade}')
            escolher_prioridade = int(input('Escolha pelo índíce a ficha prioridade:'))
            imprimeElemento(fila_prioridade, escolher_prioridade)
            removeElemento(fila_prioridade, escolher_prioridade)

            inicio('Novo Cadastro')
            nome = str(input('Nome do Cliente:'))

            while True:
                cpf = input('CPF:')
                if len(cpf) == 11:
                    if cpf.isnumeric():
                        break
                print('Digite um número válido!')

            rua = input('RUA:')
            n1 = int(input('NÚMERO:'))
            while True:
                cep = input('CEP:')
                if len(cep) == 8:
                    if cep.isnumeric():
                        break
                print('CEP inválido!')
            cidade = str(input('Cidade:'))
            estado = str(input('Estado:'))
            inicio('GERANDO NÚMERO')
            print('processando...')
            sleep(3)
            inicio('Número do cliente gerado com sucesso!')
            numero = (f'(82){999}{gerador}')
            numero_novo = numero
            print(numero_novo)

            aux = [f'Nome: {nome} - Cpf: {cpf} - Rua: {rua} - Número: {n1} - CEP: {cep} - Número Gerado {numero_novo}']

            insereElemento(cadastro, aux)

            print(len(cadastro) - 1, cadastro[len(cadastro) - 1])
            o = open(arquivo, 'at')
            o.write(f'{aux}\n')
            o.close()

            sleep(2)
            continue

    elif op == 4:
        inicio ('FILA PRIORIDADE')
        print(f'FILA PRIORIDADE:{fila_prioridade}')
        escolher_prioridade = int(input('Escolha pelo índice para chamar a ficha prioridade:'))
        imprimeElemento(fila_prioridade, escolher_prioridade)

        sleep(2)

    elif op == 5:

        o = open(arquivo, 'rt')
        print(o.read())
        o.close()
        op = menu(['Voltar'])
        if op == 1:
            continue



