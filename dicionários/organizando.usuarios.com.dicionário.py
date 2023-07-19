#organizando usuários#
import json
from funcoes import *

usuarios = {}

opcao = perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    if opcao=="P":
        buscar(usuarios)
    if opcao=="E":
        excluir(usuarios)
    if opcao=="L":
        listar(usuarios)
    opcao = perguntar()

print(usuarios)
        
f = open("bd.txt")
y = json.dumps(f)

