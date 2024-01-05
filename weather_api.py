# weather api
import requests

def check_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        humidity = data['main']['humidity']

        print(f"Temperature in {city}: {temperature} Kelvin")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")

if __name__ == "__main__":
    api_key = "8a0076deadd5be662947d91622e82670"  
    city = input("Enter city: ")

    check_weather(api_key, city)
    ''