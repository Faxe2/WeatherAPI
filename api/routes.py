

from flask import Flask, request, jsonify, abort, redirect, make_response, render_template

import functions


from . import app




@app.route('/v1/weather', methods=['GET'])
def weather_route() -> None:
    city_header = request.headers.get('city')
    if not city_header: # city header empty
       return functions.api_funcs.get_message_dict('Invalid City!')
    if functions.api_funcs.get_weather(city_header) == None:
        return functions.api_funcs.get_message_dict('Invalid City!')
    temp  = functions.api_funcs.get_weather(city_header)
    return jsonify({'temperature': f'{temp}°C'})
      