from tkinter import *
from tkinter import messagebox
import requests

def show_weather():
    city = city_entry.get()
    api_key = "3ed3dc53bb5965300bffdf6739831403" 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Show loading state
    weather_label.config(text="Loading...")
    
    response = requests.get(url)
    weather_data = response.json()


    if "message" in weather_data:
        messagebox.showerror("Error", weather_data["message"])
    else:
        weather_text = f"City: {city}\n"
        weather_text += f"Temperature: {weather_data['main']['temp']}°F\n"
        weather_text += f"Pressure: {weather_data['main']['pressure']} hPa\n"
        weather_text += f"Humidity: {weather_data['main']['humidity']}%\n"
        weather_text += f"Description: {weather_data['weather'][0]['description']}\n"
        weather_label.config(text=weather_text)


root=Tk()

root.title("Weather App")
root.geometry("400x400")

l1=Label(root, text="Enter city name: ")
l1.pack()

city_entry=Entry(root,text="")
city_entry.pack()
show_weather_button=Button(root, text="Show weather",command=show_weather)
show_weather_button.pack()
weather_label=Label(root,text="")
weather_label.pack()
root.mainloop()