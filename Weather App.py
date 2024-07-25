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

    except: #This is the except block, it will run if the try block fails
        print("Please try again with a valid location!")
        return None, None, None,None


while True:
    
    menu = input( "\nType the number next you the respect action you want completed\n" + Fore.RED + "\n(1) Current Weather" + Fore.GREEN + "\n(2) 5-day Forecast" + Fore.MAGENTA + "\n(3) Help" + Fore.LIGHTYELLOW_EX + "\n(4) History" + Fore.BLUE + "\n(5) Exit \n ") # <-- get user input for menu

    if menu == "1": # <-- check if user input is 1
        # Get weather for a location
        location = getLocation() #calls location function
        current_temp, current_weather, forecast, humidity = get_weather(location) # <-- call get_weather function with location
        #os.system("cls") # <-- clear terminal
    elif menu == "2": # <-- check if user input is 2
        location = getLocation() #calls location function
        current_temp, current_weather, forecast,humidity = get_weather(location) # <-- call get_weather function with location
        if (current_temp, current_weather, forecast, humidity) == (None, None, None, None): # <-- check if get_weather function returned None otherwise will continue code
            continue
        else:
            five_day_forecast()
    elif menu == "3": # <-- check if user input is 3
        os.system("cls") # <-- clear terminal
        print("This program will display the current weather and 5-day forecast for a location. Type the respective numbers next to the options to select them. If there are any letters in brackets, they are the options you can chose from. If you type an invalid input then the system will not accept the answer.") # <-- print help message 
        continue # <-- continue program 
    elif menu == "4": # <-- check if user input is 4
        os.system("cls")
        if History: # <-- check if history is not empty
            print("History: \n")
            for k, v in History.items(): # <-- loop through history dictionary
                print(Fore.LIGHTCYAN_EX + f'{k}: ' + Fore.MAGENTA + f'{v[0]}°C, {v[1]}, {v[2]}% humidity') # <-- print location and current weather conditions
        else:
            print("No history yet") # <-- print message if history is empty
        continue
    elif menu == "5": # <-- check if user input is 4
        exit() # <-- exit program
    else:
        print("Invalid input")
        continue



    if (current_temp, current_weather, forecast, humidity) == (None, None, None, None): # <-- check if get_weather function returned 'None', which means the location entered does not exist. If the location is invalid, the user will be directed back to the menu, otherwise will continue code  
        continue # <-- continue program

    

    decision = input( Fore.GREEN + "\nWould you like to see the current temperature and weather? (yes/no): ").lower()

    if decision == "yes": # <-- ask user if they want to see the forecast
        # Print current weather conditions
        os.system("cls") # <-- clear terminal
        print( Fore.LIGHTCYAN_EX + 'Current temperature in ' + Fore.YELLOW + f'{location}: {current_temp}') # <-- print current temperature
        print(Fore.LIGHTCYAN_EX + 'Current weather in ' + Fore.YELLOW + f'{location}: {current_weather}') # <-- print current weather
        print(Fore.LIGHTCYAN_EX + 'Humidity in ' + Fore.YELLOW + f'{location}: {humidity}%')
        time.sleep(1) # <-- wait for 1 second
    elif decision == "no":
        os.system("cls") # <-- clear terminal
        continue
    else:
        print("Invalid input")
        continue
    

    futureforcast = input("\nWould you like to see the forcast for the next 5 days? (yes/no): ")  # <-- ask user if they want to see the forecast
    if futureforcast.lower() == "no": # <-- check if user input is no
        continue # <-- continue program
    elif futureforcast.lower() == "yes":
        os.system("cls")    # <-- clear terminal
        five_day_forecast()
        time.sleep(2)
    else:
        print("Invalid input")
        continue