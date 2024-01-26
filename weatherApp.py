# Weather app project

import tkinter as tk

import requests

window = tk.Tk()

print("Welcome to my weather app!")

print("\nABOUT THIS APP:")
print("Using the OpenWeather API from RapidAPI, you can use this app to the today's current weather for any global city.")

while True:
    location = input("\nPlease enter a city: ")

    url = f"https://open-weather13.p.rapidapi.com/city/{location}&units=metric"

    headers = {
        "X-RapidAPI-Key": "1df2a02fd4mshbc648a8f22021e2p1fc2f9jsn613c4d33ca78",
        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    #print(response.json())

    if response.json()['cod'] == '404':
        print("That is an invalid location! Please enter a valid city.")
        continue

    break

low = round(response.json()['main']['temp_min'], 2)
high = round(response.json()['main']['temp_max'], 2)

print("\n~~TODAY~~")
print(f"High: {high}°C")
print(f"Low: {low}°C")
