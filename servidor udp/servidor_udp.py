# servidor udp

from socket import *

servidor = "127.0.0.1"
porta = 43214

# AF_INET = método para informar q utilizaremos o hostname e a porta
obj_socket = socket(AF_INET, SOCK_DGRAM)   # DGRAM = método para servidores udp
obj_socket.bind((servidor, porta))
print("Servidor pronto....")

while True:
    dados, origem = obj_socket.recvfrom(65535)   # range máximo de portas alcançadas
    print("Origem...........: ", origem)         # retorna a tupla dados(bytes recebidos) e origem(cliente)
    print("Dados recebidos..: ", dados.decode()) # método decode decodifica bytes em strings, no caso dados estaria em bytes
    resposta = input("Digite a resposta: ")      # quem envia a resposta é o servidor no caso de udp
    obj_socket.sendto(resposta.encode(), origem) # sendto método para enviar AO CLIENTE a resposta.encode(), pois como decodificamos
                                                 # ela para receber os bytes em strings, agr precisamos transformar em bytes de novo
    obj_socket.close()                           # para o cliente(origem) recebê-lo
