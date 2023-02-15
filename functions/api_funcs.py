import requests
from typing import Tuple, List

def get_message_dict(msg: str) -> dict:
    """
    This function returns the string msg in the dictionary format: {'Message': msg}
    """
    return {'Message': msg}
    
    
def get_weather(city: str) -> Tuple[float, str, float, float, float, float]:
    """This function gets the given city and then fetches the data from openweathermap"""
    with requests.Session() as session:
        # get city id from API
        response = session.get(f'https://openweathermap.org/data/2.5/find?q={city}&appid=439d4b804bc8187953eb36d2a8c26a02&units=metric').json()
        if 'list' not in response or not response['list']:
            return None
        city_id = response['list'][0]['id']
        # use city id to get final weather info
        final_response = session.get(f'https://openweathermap.org/data/2.5/weather?id={city_id}&appid=439d4b804bc8187953eb36d2a8c26a02').json()
        # extract relevant data from response
        temp, desc, pressure, humidity = final_response['main']['temp'], final_response['weather'][0]['description'], final_response['main']['pressure'], final_response['main']['humidity']
        longitude, latitude, temp_min, temp_max = final_response['coord']['lon'], final_response['coord']['lat'], final_response['main']['temp_min'], final_response['main']['temp_max']
        # return a tuple of relevant data
        return temp, desc, pressure, humidity, longitude, latitude, temp_min, temp_max
