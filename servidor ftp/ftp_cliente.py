#ftp cliente

from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario = input("Digite o usuario: ")

senha = input("Digite a senha: ")

ftp.login(usuario, senha) # método login onde eu passo as vars usuario e senha

print("Diretório atual de trabalho: ", ftp.pwd())

# após o login, o método pwd vai me informar o diretório da máquina logada

ftp.cwd('pub')

# o método cwd me faz navegar até o diretório desejado, neste caso a pasta 'pub'

print("Diretório corrente: ", ftp.pwd())

# confirmando diretório

print(ftp.retrlines('LIST'))

# método retrlines com comando LIST para listar os arquivos q estão naquele diretório
# neste caso retorna o conteudo da pasta pub(pública) no ftp ibiblio.org

ftp.quit()
