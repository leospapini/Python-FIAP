#primeiros passos com API's

from geopy.geocoders import GoogleV3

endereco = 'avenida alberto byington, 712 Sao Paulo'
resultado = GoogleV3(api_key='AIzaSyB2JsKL-Q00Pea5gIcJ7dSa6XPBFWfF3uQ')  
location = resultado.geocode(endereco)

print(location)

#aqui percebemos q o próprio geocode já atualiza o endereço com
#tudo q estiver faltando, bairro, cep e etc..
