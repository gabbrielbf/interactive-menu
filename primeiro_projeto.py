import time
import re

def exibir_carregamento(mensagem="Carregando"):
    """ função para exibir um carregamento animado a cada execução do programa """

    print(f"\n{mensagem}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(0.5)
    print('\nSucesso!\n')

def menu_interativo():
    """ função para exibir um menu interativo e retornar uma opção numérica """

    print('=' * 89)
    print(' Participantes - EVENTO ABC ')
    print('=' * 89)
    print('1 - Cadastrar participante')
    print('2 - Listar participantes')
    print('3 - Atualizar participante')
    print('4 - Remover participante')
    print('0 - Sair')
    print('=' * 89)
    try:
        return int(input('Digite qual opção deseja escolher: '))
    except ValueError:
        return -1

def validar_nome():
    """ função para fazer uma validação de APENAS NOMES COM LETRAS, sem números ou espaços, conver
    tendo os mesmos para letra maiúscula cada primeiro caractere """

    while True:
        nome = input('Digite o nome do participante: ').strip().title()
        if nome and not re.findall(r'[^a-zA-Zà-úÀ-Ú\s]', nome):
            return nome
        print('[❌ERRO]! Digite apenas nomes válidos.')

def listar_participantes(lista):
    """ listar os participantes da lista (caso exista algum nela) """

    if not lista:
        print('[❌ERRO]! Nenhum participante cadastrado!\n')
        return False
    print('=' * 89)
    print('Lista de participantes inscritos:')
    for i, nome in enumerate(lista):
        print(f'{i + 1} - {nome}')
    print('=' * 89)
    return True

def cadastrar_participante(lista):
    """ cadastrar participante com a validação de nome """

    exibir_carregamento()
    while True:
        lista.append(validar_nome())
        print('✅ Usuário adicionado!')
        if input('\nDeseja incluir mais alguém? [S/N]: ').lower() != 's':
            break

def atualizar_participante(lista):
    """ atualizar um participante existente na lista a partir de seu índice """

    if not listar_participantes(lista): 
        return
    try:
        indice = int(input(f'Digite o número (1 a {len(lista)}) que deseja alterar: ')) - 1
        if 0 <= indice < len(lista):
            lista[indice] = validar_nome()
            print('✅ Lista atualizada com sucesso!')
        else:
            print('[❌ERRO]! Índice inválido.')
    except ValueError:
        print('[❌ERRO]! Entrada inválida.')

def remover_participante(lista):
    """ remover participante da lista a partir de seu índice """

    if not listar_participantes(lista): return
    try:
        indice = int(input(f'Digite o número (1 a {len(lista)}) de quem deseja remover: ')) - 1
        if 0 <= indice < len(lista):
            removido = lista.pop(indice)
            print(f'✅ O Participante ({removido}) foi removido com sucesso!')
        else:
            print('[❌ERRO]! Índice inválido.')
    except ValueError:
        print('[❌ERRO]! Entrada inválida.')

def main():
    """ código principal, enxuto e refatorado """

    lista = []
    while True:
        decisao = menu_interativo()
        
        if decisao == 0:
            if input('Deseja encerrar o sistema [S/N]? ').lower() == 's':
                print('\nPrograma encerrado.')
                break
        elif decisao == 1:
            cadastrar_participante(lista)
        elif decisao == 2:
            listar_participantes(lista)
            input('Pressione Enter para voltar ao menu...')
        elif decisao == 3:
            atualizar_participante(lista)
        elif decisao == 4:
            remover_participante(lista)
        else:
            print('[❌ERRO]! Opção inválida.\n')

if __name__ == "__main__":
    main()