#primeiros passos com API's

from geopy.geocoders import GoogleV3

endereco = '874, Augusto de Toledo, São Caetano do Sul, SP'
geolocator = GoogleV3(api_key='YOUR API')
location = geolocator.geocode(endereco)
print((location.latitude, location.longitude))

#retorna (-23.6215126, -46.5668982) que é a localização global da minha casa
