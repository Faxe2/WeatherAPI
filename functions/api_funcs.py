


import requests as r
from typing import Tuple, List
import json





def get_message_dict(msg: str) -> dict:
    """
    This Function Returns The String Msg in the dictionary m, so it will look like this: {'Message': msg}
    """
    
    
    m: dict = {'Message': msg}
    
    return m
    
    
    

def get_weather(city: str) -> None:
    """ This Function gets the given city and then fetches the data from openweathermap"""
    url = r.get(f'https://openweathermap.org/data/2.5/find?q={city}&appid=439d4b804bc8187953eb36d2a8c26a02&units=metric')
    get_json = json.loads(url.text) 
    if get_json['count'] == 0:
        return None
    elif len(get_json['list']) == 0:
        return None
    else:
        city_id = get_json['list'][0]['id']
            
        final_url = r.get(f'https://openweathermap.org/data/2.5/weather?id={city_id}&appid=439d4b804bc8187953eb36d2a8c26a02')
            
        get_final_json = json.loads(final_url.text)
            
        temp = get_final_json['main']['temp']
        #weather_description = get_final_json['weathe']
            
            
        return temp   
   
    