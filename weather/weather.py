import requests
from config import config

params = config('config.ini', 'env')

def parseWeather(data):
    parsed_data = {
        "location": {
            'city': data['location']['name'],
            'country': data['location']['country'],
        },
        "current": {
            'temp_c': data['current']['temp_c'],
            'condition': data['current']['condition']['text'],
            'wind_kph': data['current']['wind_kph'],
            'humidity': data['current']['humidity'],
        },
        "forecast": {
            'date': data['forecast']['forecastday'][0]['date'],
            'max_temp_c': data['forecast']['forecastday'][0]['day']['maxtemp_c'],
            'min_temp_c': data['forecast']['forecastday'][0]['day']['mintemp_c'],
            'condition': data['forecast']['forecastday'][0]['day']['condition']['text'],
        },
        "hourly" : [
            {
                'time': hour['time'],
                'temp_c': hour['temp_c'],
                'condition': hour['condition']['text'],
                'wind_kph': hour['wind_kph'],
                'humidity': hour['humidity']
            }
            for hour in data['forecast']['forecastday'][0]['hour']
        ]
    }
    return parsed_data

def get_weather(coords):
    response = requests.get(f"{params['api_url']}/forecast.json?key={params['weather_api']}&q={coords}&days=1")
    if response.status_code == 200:
        data = response.json()
        print(f"Weather data for {data['location']['name']} fetched successfully.")
        return parseWeather(data)
    else:
        print(f"Failed to fetch weather data for {city}. Status code: {response.status_code}")
        print("Response:", response.text)
        return

if __name__ == "__main__":
    city = "Birmingham"
    get_weather(city)

        