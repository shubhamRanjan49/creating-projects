import requests

city = input("enter the city name : \n")

url = f"https://api.weatherapi.com/v1/current.json?key=045d1d5bb49f4079ae633309241108q={city}"
r = requests.get(url)
print (r.text)