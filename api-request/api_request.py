import requests
api_key = "your_api_key"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching weather data from Weatherstack...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        raise
