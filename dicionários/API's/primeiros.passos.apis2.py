#primeiros passos com API's

from geopy.geocoders import GoogleV3

endereco = 'avenida alberto byington, 712 Sao Paulo'
resultado = GoogleV3(api_key='YOUR API')  
location = resultado.geocode(endereco)

print(location)

#aqui percebemos q o próprio geocode já atualiza o endereço com
#tudo q estiver faltando, bairro, cep e etc..
