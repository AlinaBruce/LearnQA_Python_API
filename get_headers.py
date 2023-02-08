import requests

headers = {"some_header" : "123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers" , headers = headers)

print(response.text) # получаем заголовки запроса
print(response.headers) # получаем заголовки ответа

# go to http://jsonviewer.stack.hu to convert to normal format


