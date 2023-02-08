import requests

#https://playground.learnqa.ru/api/map отсюда url
#важно писать именно data, ибо иначе у нас не будет ничего в итоге, кроме get запроса
response = requests.post("https://playground.learnqa.ru/api/check_type", data = {"param1" : "value1"})

print(response.text)