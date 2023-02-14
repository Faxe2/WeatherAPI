import requests






city = input("By: ")

headers = {
    'city': city
}


url = requests.get('http://127.0.0.1:5000/v1/weather', headers=headers)
print(url.text)