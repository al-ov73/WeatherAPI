import requests


# s_city = "Ulyanovsk (RU)"
city_id = 479119
appid = "f9c970b644cece4b3ace8d77637b70f4"

# Проверка наличия в базе информации о нужном населенном пункте

# s_city = "Petersburg,RU"
# city_id = 0
# appid = "буквенно-цифровой APPID"
# try:
#     res = requests.get("http://api.openweathermap.org/data/2.5/find",
#                  params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
#     data = res.json()
#     cities = ["{} ({})".format(d['name'], d['sys']['country'])
#               for d in data['list']]
#     print("city:", cities)
#     city_id = data['list'][0]['id']
#     print('city_id=', city_id)
# except Exception as e:
#     print("Exception (find):", e)
#     pass


try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print(f'full response: {data}')
    print(' ')
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'], "ощущается как:", data['main']['feels_like'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass

