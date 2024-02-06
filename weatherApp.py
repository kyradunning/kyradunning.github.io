# Weather app project

import tkinter as tk
from tkinter import *

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
window.geometry("750x500")

# Background Image File
bg = PhotoImage(file = "images/weather-app-background2.png")
background_canvas = Canvas( window, width = 750, height = 500)
background_canvas.pack(fill = "both", expand = True)
background_canvas.create_image( 0, 0, image = bg, anchor = "nw")

# Header label
header = tk.Label(window, text="Welcome to my weather app!")
header.pack()

# Paragraph text label
about = background_canvas.create_text( 200, 250, text = "\nUsing the OpenWeather API from RapidAPI, \nyou can use this app to see today's weather for any global city.")
paragraphVar = tk.Label(window, text=about)
paragraphVar.pack()

# City input
#label = background_canvas.create_text( 200, 250, text = "Please enter a city: ")
#label_city = tk.Label(window, label)
label_city = tk.Label(window, text='\nPlease enter a city: ')
label_city.pack()

# Input functionality
e1 = tk.Entry(window)
e1.pack()

# Fetching weather information
location_button = Button( window, text = "Okay", command=get_weather) # Creating button
location_button_canvas = background_canvas.create_window( 100, 10, anchor = "nw", window = location_button) # Displaying button
#location_button = tk.Button(window, text='Okay', width=10, command=get_weather)
location_button.pack()

# Display weather information
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()