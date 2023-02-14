from flask import Flask, request, jsonify
import functions
from . import app

@app.route('/v1/weather', methods=['GET'])
def weather_route() -> None:
    city_header = request.headers.get('city')
    if not city_header:
       return functions.api_funcs.get_message_dict('Invalid City!')
   
    weather_info = functions.api_funcs.get_weather(city_header)
    if weather_info is None:
        return functions.api_funcs.get_message_dict('Invalid City!')
    
    temp, description, pressure, humidity, longitude, latitude = weather_info
    
    json_data = dict(
        location=dict(
            name=city_header,
            latitude=latitude,
            longitude=longitude
        ),
        weather=dict(
            temperature=temp,
            humidity=humidity,
            pressure=pressure,
            description=description
        )
    )
    
    return jsonify(json_data)