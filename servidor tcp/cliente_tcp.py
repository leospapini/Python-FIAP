#cliente tcp

from socket import *

servidor = "127.0.0.1" #localhost
porta = 43210

msg = bytes(input("Digite algo: "), 'utf-8')
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor,porta))
obj_socket.send(msg)
resposta = obj_socket.recv(1024)
print("Recebemos: ", resposta)
obj_socket.close()

#ao conectar com o servidor e enviar a mensagem ou qualquer coisa q precise
#é notificado pelo próprio servidor q a mensagem foi recebida, característica
#do protocolo tcp
