#primeiro ftp

from ftplib import *

ftp = FTP('ftp.ibiblio.org')

print(ftp.getwelcome())

ftp.quit()

#retorna 220 ProFTPD Server, q significa q o ftp foi conectado com sucesso no
#servidor
