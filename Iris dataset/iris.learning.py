basedados = []

with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))

print(basedados)

print(float(basedados[0][0]) + float(basedados[0][1]))

#aqui em cima somamos o conteudo 0 (5.1) da primeira lista dentro da lista
#iris.data com o conteudo 1 (3.6) = 8.6
