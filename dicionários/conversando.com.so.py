#conversando com so usando platform

import platform #importamos a biblioteca platform quando queremos
                #nos comunicar com o SO local
from datetime import datetime #usamos from datetime import datetime
                              #para importar da biblioteca datetime
                              #o datetime, ou seja, data e horário atual
                              #no formato americano
import getpass

print("Nome maquina:...........", platform.node())
print("Arquitetura:............", platform.architecture())
print("Sistema Operacional:....", platform.system())
print("Versao do SO:...........", platform.release())
print("Processador:............", platform.processor())
print("Versao do Python:.......", platform.python_version())


print("Data e horário vigente:.", datetime.now())

print("Usuário da máquina:.....", getpass.getuser())#retorna o usuário

print("Usuário da máquina:.....", getpass.getip())


