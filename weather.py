import requests
from config import config

params = config('config.ini', 'env')

def get_weather(city):
    response = requests.get(f"{params['api_url']}/current.json?key={params['weather_api']}&q={city}")
    if response.status_code == 200:
        print(response.json())
    else:
        return

if __name__ == "__main__":
    city = "Birmingham"
    get_weather(city)