import requests
import json
import os
import time
from colorama import * # <-- import colorama module


# API Key for OpenWeatherMap
api_key = '070306651cab27e069e10f0fa4d473e3' # <-- replace with your API key
History = {}

def getLocation():#
    os.system('cls') # <-- clear terminal
    l = input("Enter a location: ") # <-- get location from user
    return l 

# Function to save location to history
def save_history(query: str, current_temp, current_weather, humidity):
    global History 
    History[query] = (current_temp, current_weather, humidity) # <-- add location to history dictionary

def five_day_forecast(): # <-- function to print 5-day forecast
        print("\n5-day forecast:") # <-- print header
        print("{:<20} {:<20} {:<20}".format(Fore.RED + 'Date','Temp','Weather')) # <-- print header
        print("{:<20} {:<20} {:<20}".format(Fore.BLACK + '==========','==========','===============')) 
        for date, weather in forecast.items(): # <-- loop through forecast dictionary
            print("{:<20} {:<20} {:<20}".format ( Fore.CYAN + f'{date}',f'{weather["temp"]}',f'{weather["weather"]}'))# <-- print date, temperature, and weather
    
        

# Function to get current weather conditions and 5-day forecast
def get_weather(location):
    try: 
        # This line tries to run the code below, if it fails, it will run the except block
        # API endpoint for current weather
        current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        # API endpoint for 5-day forecast
        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric' 

    # Make GET request to API
        current_weather_response = requests.get(current_weather_url)
        forecast_response = requests.get(forecast_url)
    
        # Parse JSON response
        current_weather_data = json.loads(current_weather_response.text) # <-- convert JSON response to Python dictionary
        forecast_data = json.loads(forecast_response.text) # <-- convert JSON response to Python dictionary
        
        # Extract current weather conditions
        current_temp = current_weather_data['main']['temp'] # <-- extract temperature from dictionary
        current_weather = current_weather_data['weather'][0]['description'] # <-- extract weather description from dictionary
        humidity = current_weather_data['main']['humidity']
        
        # Extract forecast for next 5 days
        forecast_list = forecast_data['list'] # <-- extract list of forecasts from dictionary

        forecast = {} # <-- create empty dictionary to store forecast
        for f in forecast_list: # <-- loop through list of forecasts
            date = f['dt_txt'][:10] # <-- extract date from forecast
            if date not in forecast: # <-- check if date is already in forecast dictionary
                forecast[date] = { 
                    'temp': f['main']['temp'],
                    'weather': f['weather'][0]['description']
                }
        save_history(location, current_temp, current_weather, humidity) # <-- call save_to_history function to add location to history
        return current_temp, current_weather, forecast, humidity # <-- return current weather conditions and 5-day forecast2n
