#primeiro servidor com socket TCP

from socket import *

servidor = "127.0.0.1" #localhost
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM feito para trabalhar no TCP
obj_socket.bind((servidor,porta)) #seta endereço + porta
obj_socket.listen(2) #quantidade de maquinas q conseguirão utilizar/escutar o server

print("Aguardando cliente....")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024)) #recv = método receive 1024 é o tamanho do pacote em bytes
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah cliente' #retorno de mensagem recebida
        con.send(msg_enviada) #método send para enviar a mensagem pra conexão con
        break
    con.close()
