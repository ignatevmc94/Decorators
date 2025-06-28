import time
import requests
from decor1 import logger

@logger
def find_uk_city(coordinates:list) -> str:
    """Ваш код здесь"""
    token = '67ed14bef1a93811544498ebi64de96'
    cities = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    for latitude, longitude in coordinates:
        url = f'https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}&api_key={token}'
        response = requests.get(url).json()
        city = response['address']['city']
        time.sleep(1)
        if city in cities:
            return city

coord = [('55.7514952', '37.618153095505875'),
              ('52.3727598', '4.8936041'),
              ('53.4071991', '-2.99168')
        ]

city = find_uk_city(coord)
print(city)



# if __name__ == '__main__':
#     _coordinates = [
#         ('55.7514952', '37.618153095505875'),
#         ('52.3727598', '4.8936041'),
#         ('53.4071991', '-2.99168')
#     ]
#     assert find_uk_city(_coordinates) == 'Liverpool'
