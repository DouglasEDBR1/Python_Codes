#Projeto de cadastro utilizando estrutura de dados, com ávore binária e fila.

#RESUMO...
#Sistema de uma biblioteca que vefica a dispobilidade do livro, cadastro de dados dos clientes com
#arquivo txt, a busca pelo livro efetuada com árvore binária"




from time import sleep

def linha(tam=60):
    return '=' * 60


def inicio(txt):
    print(linha())
    print(txt.center(60))
    print(linha())


def menu_principal(lista):
    inicio('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opcao = tratativa_de_erro('Opção:')
    return opcao


def menu(lista):
    inicio('MENU')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opcao = tratativa_de_erro('Opção:')
    return opcao


def tratativa_de_erro(txt):
    while True:
        try:
            n1 = int(input(txt))
        except(ValueError, TypeError):
            print('Digite uma opção válida!')
            continue
        else:
            return n1


def buscaElemento(vArvore, valor, indice):
    if vArvore[indice]['CÓDIGO'] == valor:
        return indice
    elif valor > vArvore[indice]['CÓDIGO'] and vArvore[indice]['DIREITA'] > 0:
        return buscaElemento(vArvore, valor, vArvore[indice]['DIREITA'])
    elif valor < vArvore[indice]['CÓDIGO'] and vArvore[indice]['ESQUERDA'] > 0:
        return buscaElemento(vArvore, valor, vArvore[indice]['ESQUERDA'])
    else:
        return -1


def exibir_livro_na_arvore(vArvore, valor):
    buscar = buscaElemento(vArvore, valor, 0)
    if buscar >= 0:
        print('LIVRO:', vArvore[buscar]['LIVRO'])
        print('STATUS:', vArvore[buscar]['STATUS'])
    else:
        print('Esse livro não está disponível!')


def exibir_livro_na_arvore2(vArvore, valor):
    buscar = buscaElemento(vArvore, valor, 0)
    if buscar >= 0:
        return vArvore[buscar]['LIVRO']


def getPai(vArvore, valor, indice):
    if valor > vArvore[indice]['CÓDIGO'] and vArvore[indice]['DIREITA'] > 0:
        return getPai(vArvore, valor, vArvore[indice]['DIREITA'])
    elif valor < vArvore[indice]['CÓDIGO'] and vArvore[indice]['ESQUERDA'] > 0:
        return getPai(vArvore, valor, vArvore[indice]['ESQUERDA'])
    else:
        return indice


def insereElemento(vArvore, valor, livro, status):
    if vArvore == {}:
        no = {'CÓDIGO': valor, 'LIVRO': livro, 'STATUS': status, 'ESQUERDA': 0, 'DIREITA': 0}
        aux = {len(vArvore): no}
        vArvore.update(aux)

    elif buscaElemento(vArvore, valor, 0) >= 0:
        print(f'O VALOR {valor} JÁ EXISTE NA ÁRVORE!')

    else:
        noPai = getPai(vArvore, valor, 0)

        if valor < vArvore[noPai]['CÓDIGO']:
            vArvore[noPai]['ESQUERDA'] = len(vArvore)
        else:
            vArvore[noPai]['DIREITA'] = len(vArvore)

        no = {'CÓDIGO': valor, 'LIVRO': livro, 'STATUS': status, 'ESQUERDA': 0, 'DIREITA': 0}
        aux = {len(vArvore): no}
        vArvore.update(aux)


def organizarElmentos(vArvore, indice):
    livros = []
    valores = []
    status = []
    for i in range(0, len(vArvore)):
        if i != indice:
            valores.append(vArvore[i]['CÓDIGO'])
            livros.append(vArvore[i]['LIVRO'])
            status.append(vArvore[i]['STATUS'])

    vArvore.clear()
    for i in range(0, len(valores)):
        insereElemento(vArvore, valores[i], livros[i], status[i])


def removerElemento(vArvore, valor):
    indice = buscaElemento(vArvore, valor, 0)
    if indice >= 0:
        organizarElmentos(vArvore, indice)

    else:
        print(f'O VALOR {valor} NÃO EXISTE NA ÁRVORE!')


def criar_arquivo(nome):
    c = open(nome, 'wt+')
    c.close()


def verificar_arquivo(nome):
    try:
        n = open(nome, 'rt')
        n.close()
    except FileNotFoundError:
        return False
    else:
        return True


arquivo = 'historico.txt'
if not verificar_arquivo(arquivo):
    criar_arquivo(arquivo)

arvore = {}

insereElemento(arvore, 50, 'Harry Potter', 'INDISPONÍVEL')
insereElemento(arvore, 15, 'O Código da Vinci', 'DISPONÍVEL')
insereElemento(arvore, 20, 'Sherlock Holmes', 'INDISPONÍVEL')
insereElemento(arvore, 30, 'O Morro dos Ventos Ruivantes', 'DISPONÍVEL')
insereElemento(arvore, 60, 'O Peregrino', 'DISPONÍVEL')
insereElemento(arvore, 70, 'A Menina Que Roubava Livros', 'DISPONÍVEL')
insereElemento(arvore, 80, 'Alice no País das Maravilhas', 'DISPONÍVEL')
insereElemento(arvore, 55, 'Assassins Creed', 'INDISPONÍVEL')
insereElemento(arvore, 19, 'O Poder do Hábito', 'DISPONÍVEL')
insereElemento(arvore, 100, 'Contato', 'DISPONÍVEL')
insereElemento(arvore, 79, 'Reino do Amanhã', 'Indisponível')
insereElemento(arvore, 12, 'O Pequeno Príncipe', 'DISPONÍVEL')
insereElemento(arvore, 52, 'O Advogado do Diabo', 'DISPONÍVEL')
insereElemento(arvore, 65, 'All-Stars Superman', 'DISPONÍVEL')
insereElemento(arvore, 59, 'Soul Calibur', 'DISPONÍVEL')
insereElemento(arvore, 21, 'Tekken', 'DISPONÍVEL')
insereElemento(arvore, 13, 'Lanterna Verde', 'DISPONÍVEL')




# for a in arvore:
#    print(a, arvore[a])

while True:

    op = menu_principal(['Escolher Livro', 'Devolução', 'Histórico', 'Ver Árvore Binária'])

    if op == 1:
        while True:
            for i in range(0, (len(arvore))):
                print('CÓDIGO:', arvore[i]['CÓDIGO'], '|', 'LIVRO:', arvore[i]['LIVRO'], '|', 'STATUS:',
                      arvore[i]['STATUS'])

            inicio('Escolha seu livro')
            try:
                escolher_livro = int(input('Para selecionar, digite o código do livro: '))
            except(ValueError, TypeError):
                inicio('Digite uma opção válida!')
                sleep(3)
                continue
            else:
                pass
            exibir_livro_na_arvore(arvore, escolher_livro)
            if buscaElemento(arvore, escolher_livro, 0) == -1:
                inicio('Código inválido! Digite um código válido.')
                sleep(3)
                continue

            buscar2 = buscaElemento(arvore, escolher_livro, 0)
            if buscar2 >= 0:
                if arvore[buscar2]['STATUS'] == 'INDISPONÍVEL':
                    sleep(2)
                    inicio('Infelizmento o livro está indisponível!')
                    sleep(3)
                    continue
                else:
                    break

            confirmar = menu(['Confirmar', 'Não Confirmar'])
            if confirmar == 1:
                break
            elif confirmar == 2:
                continue
            else:
                print('Digite uma opção válida!')
                continue

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

        livro = exibir_livro_na_arvore2(arvore, escolher_livro)
        print(escolher_livro, livro)
        inicio('Confirme Seus Dados')
        print('NOME:', nome, '| CPF:', cpf, '| RUA', rua, 'Nº', n1, '| LIVRO:', livro)
        sleep(2)

        confirmar = menu(['Confirmar', 'Não Confirmar'])
        if confirmar == 1:
            removerElemento(arvore, escolher_livro)
            insereElemento(arvore, escolher_livro, livro, 'INDISPONÍVEL')
            inicio('Concluído! Tenha uma boa leitura!')
            aux = [f'Nome: {nome} - CPF: {cpf} - Rua: {rua} {n1} - CEP: {cep} - Alugando Livro: {livro}']
            o = open(arquivo, 'at')
            o.write(f'{aux}\n')
            o.close()
            sleep(2)
            pass

        elif confirmar == 2:
            inicio('Cadastro desfeito!')
            sleep(2)
            continue

        else:
            print('Digite uma opção válida!')
            continue

    elif op == 2:
        while True:
            for i in range(0, (len(arvore))):
                print('CÓDIGO:', arvore[i]['CÓDIGO'], '|', 'LIVRO:', arvore[i]['LIVRO'], '|', 'STATUS:',
                      arvore[i]['STATUS'])

            inicio('DEVOLUÇÃO')
            try:
                escolher_livro = int(input('Digite o código para devolução do livro: '))
            except(ValueError, TypeError):
                inicio('Digite uma opção válida!')
                sleep(3)
                continue
            else:
                pass
            exibir_livro_na_arvore(arvore, escolher_livro)
            if buscaElemento(arvore, escolher_livro, 0) == -1:
                inicio('Código não localizado, digite o código corretamente.')
                sleep(3)
                continue

            buscar2 = buscaElemento(arvore, escolher_livro, 0)
            if buscar2 >= 0:
                if arvore[buscar2]['STATUS'] == 'DISPONÍVEL':
                    sleep(2)
                    inicio('Este livro já se encontra na biblioteca!')
                    sleep(3)
                    continue
                else:
                    break

        confirmar = menu(['Confirmar', 'Não Confirmar'])
        if confirmar == 1:
            pass
        elif confirmar == 2:
            continue
        else:
            print('Digite uma opção válida!')
            continue

        inicio('Confirmação de Devolução')

        nome = str(input('Nome do Cliente:'))
        while True:
            cpf = input('CPF:')
            if len(cpf) == 11:
                if cpf.isnumeric():
                    break
            print('Digite um número válido!')

        livro = exibir_livro_na_arvore2(arvore, escolher_livro)

        confirmar = menu(['Confirmar', 'Não Confirmar'])
        if confirmar == 1:
            aux = [f'Nome: {nome} - CPF: {cpf} - Devolução do Livro: {livro}']
            o = open(arquivo, 'at')
            o.write(f'{aux}\n')
            o.close()
            removerElemento(arvore, escolher_livro)
            insereElemento(arvore, escolher_livro, livro, 'DISPONÍVEL')
            print(escolher_livro, livro)
            inicio('DEVOLVIDO!')
            sleep(2)
            inicio('Obrigado e volte sempre!')
            pass

        elif confirmar == 2:
            inicio('Devolução não confirmada!')
            sleep(2)
            continue

        else:
            print('Digite uma opção válida!')
            continue


    elif op == 3:
        o = open(arquivo, 'rt')
        print(o.read())
        o.close()
        while True:
            op = menu(['Voltar'])
            if op == 1:
                break
            else:
                inicio('Digite uma opção válida!')
                sleep(2)
                continue
    elif op == 4:
        for a in arvore:
            print(a, arvore[a])
            print()
        while True:
            op = menu(['Voltar'])
            if op == 1:
                break
            else:
                inicio('Digite uma opção válida!')
                sleep(2)
                continue
    else:
        inicio('Digite uma opção válida!')
        sleep(2)
        continue