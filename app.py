import sys
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()

        current = data["current_condition"][0]
        temp = current["temp_C"]
        condition = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]

        print(f"\n🌤️  Weather in {city.capitalize()}:")
        print(f"   - Temperature: {temp}°C")
        print(f"   - Condition:   {condition}")
        print(f"   - Humidity:    {humidity}%\n")

    except requests.exceptions.HTTPError:
        print(f"❌ Error: City '{city}' not found or API error.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) >1:
        city_name = " ".join(sys.argv[1:])
    else:
        city_name = input("Enter a city name: ")

    get_weather(city_name)