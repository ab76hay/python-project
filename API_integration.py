import requests

# Replace with your API key (get from OpenWeatherMap)
API_KEY = "080c41e060f5bcbbef6ff91662bca782"
city = input("Enter city name: ")

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)

    # Check response status
    if response.status_code == 200:
        data = response.json()

        # Extract data
        city_name = data["name"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        # Display output
        print(f"\n📍 City: {city_name}")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"🌤️ Weather: {weather}")
        print(f"💧 Humidity: {humidity}%")

    else:
        print("❌ Error: Unable to fetch data. Check city name or API key.")

except Exception as e:
    print("❌ Something went wrong:", e)