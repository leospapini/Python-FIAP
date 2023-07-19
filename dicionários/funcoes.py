#funções#

def perguntar():
    return input("O que deseja realizar?\n" +
                "<I> - Para Inserir um usuário\n" +
                "<P> - Para Pesquisar um usuário\n" +
                "<E> - Para Excluir um usuário\n" +
                "<L> - Para Listar um usuário: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)

def buscar(dicionario):
    usuario=input("Digite o nome de usuário: ")
    if usuario.upper() in dicionario:
        print(f'Usuário = {usuario.upper()} e informações do usuário: {dicionario[usuario.upper()]}')
    else:
        print("Não existem usuários com este login")


def excluir(dicionario):
    usuario=input("Digite o nome de usuário: ")
    if usuario.upper() in dicionario:
        del dicionario[usuario.upper()]
        with open("bd.txt", "d") as arquivo:
            for chave in dicionario.keys():
                arquivo.delete(chave)
    else:
        print("Não existem usuários com este login")    

    
def listar(dicionario):
    usuario=input("Digite o nome de usuário: ")
    for login in dicionario.keys(): 
        if usuario.upper()==login:
            print(dicionario[login])
        else:
            print("Não existem usuários com este login")

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(f'\n{chave} : {str(valor)}')
    arquivo.close()


