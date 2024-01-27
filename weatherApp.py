# Weather app project

import tkinter as tk

import requests


def get_weather():
    location = e1.get()

    url = f"https://open-weather13.p.rapidapi.com/city/{location}&units=metric"

    headers = {
        "X-RapidAPI-Key": "1df2a02fd4mshbc648a8f22021e2p1fc2f9jsn613c4d33ca78",
        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    print(response.json())

    if response.json()['cod'] == '404':
        print("That is an invalid location! Please enter a valid city.")

    elif response.json()['cod'] == '401':
        print("Failed to fetch weather data.")

    else:
        low = round(response.json()['main']['temp_min'], 2)
        high = round(response.json()['main']['temp_max'], 2)
        result_label.config(text=f"\n~~TODAY~~\nHigh: {high}°C\nLow: {low}°C")

# Application window creation
window = tk.Tk()
window.title("Today's Weather")

# Header label
header = tk.Label(window, text="Welcome to my weather app!")
header.pack()

# Paragraph text label
about_title = '\nABOUT THIS APP:'
about = "\nUsing the OpenWeather API from RapidAPI, you can use this app to see today's weather for any global city."
paragraphVar = tk.Label(window, text=about_title+about)
paragraphVar.pack()

# City input
label_city = tk.Label(window, text='\nPlease enter a city: ')
label_city.pack()

# Input functionality
e1 = tk.Entry(window)
e1.pack()

# Fetching weather information
location_button = tk.Button(window, text='Okay', width=10, command=get_weather)
location_button.pack()

# Display weather information
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()