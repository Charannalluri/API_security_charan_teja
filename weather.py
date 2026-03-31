import os
import requests
from dotenv import load_dotenv

# Task 1: Load variables from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    # Task 3: Privacy Protection
    # We do not log the 'city' variable to the console or internal logs.
    # Under HIPAA and GDPR, location data can be considered PII (Personally 
    # Identifiable Information) or PHI when linked to healthcare patterns.
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    try:
        response = requests.get(url)
        
        # Task 2: Handle Rate Limiting (429) and other errors
        if response.status_code == 429:
            return "Error: API limit reached. Please try again in a minute."
        elif response.status_code == 404:
            return "Error: City not found."
        
        response.raise_for_status() # Catch other HTTP errors
        data = response.json()

        # Clean output for the patient
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"The current weather in the requested location is {temp}°C with {desc}."

    except requests.exceptions.RequestException as e:
        return "System Error: Unable to fetch weather alerts at this time."

if __name__ == "__main__":
    # Example usage
    weather_data = get_weather("Chennai")
    print(weather_data)
