from flask import Flask, request, jsonify
import functions
from . import app

# Create a dictionary to store the cached responses for each city header
url_cache = {}

# Define the route for '/v1/weather' with HTTP method GET
@app.route('/v1/weather', methods=['GET'])
def weather_route() -> None:
    # Get the 'city' header from the request
    city_header = request.headers.get('city')
    # If the 'city' header is missing or empty
    if not city_header:
        # Store the error message in the cache dictionary for this city header
        url_cache[city_header] = functions.api_funcs.get_message_dict('Invalid City!')
        # Return the error message as a response
        return functions.api_funcs.get_message_dict('Invalid City!')
    
    # If the 'city' header is already in the cache dictionary
    if city_header in url_cache:
        # Return the cached response for this city header
        return url_cache[city_header]

    # Get the weather information for the given city header using a function from the 'functions' module
    weather_info = functions.api_funcs.get_weather(city_header)
    # If there is no weather information for the given city header
    if weather_info is None:
        # Store the error message in the cache dictionary for this city header
        url_cache[city_header] = functions.api_funcs.get_message_dict('Invalid City!')
        # Print the cache dictionary for debugging purposes
        print(url_cache)
        # Return the error message as a response
        return functions.api_funcs.get_message_dict('Invalid City!')
    # Print the cache dictionary for debugging purposes
    print(url_cache)
    # Extract the weather information and store it in a dictionary
    temp, description, pressure, humidity, longitude, latitude, temp_min, temp_max = weather_info
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
            temp_min=temp_min,
            temp_max=temp_max,
            description=description
        )
    )
    # Cache the weather information in the cache dictionary for this city header
    url_cache[city_header] = jsonify(json_data)
    # Print the cache dictionary for debugging purposes
    print(url_cache)
    # Return the cached response for this city header
    return url_cache[city_header]