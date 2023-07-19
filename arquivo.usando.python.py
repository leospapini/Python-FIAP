#exemplo de criação de arquivo usando python#

with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
