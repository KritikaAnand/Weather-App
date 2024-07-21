import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    try:
        location = geolocator.geocode(city)
        if location:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")

            # Fetch weather information
            api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=8097a838162fbe1c11a4edf1203e971f"
            response = requests.get(api)
            
            if response.status_code == 200:
                json_data = response.json()
                condition = json_data['weather'][0]['main']
                description = json_data['weather'][0]['description']
                temp = int(json_data['main']['temp'] - 273.15)
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']

                t.config(text=f"{temp}°C")
                c.config(text=f"{condition} | Feels Like {temp}°C")
                w.config(text=f"{wind} m/s")
                h.config(text=f"{humidity}%")
                d.config(text=description)
                p.config(text=f"{pressure} hPa")
            else:
                messagebox.showerror("Error", f"Failed to get weather data. Status code: {response.status_code}")
        else:
            messagebox.showerror("Error", "City not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Search box
Search_image = tk.PhotoImage(file="E:/Weather APP in PYTHON/ImageS/search.png")
myImage = tk.Label(image=Search_image)
myImage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = tk.PhotoImage(file="E:/Weather APP in PYTHON/ImageS/search_icon.png")
myimage_icon = tk.Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
Logo_image = tk.PhotoImage(file="E:/Weather APP in PYTHON/ImageS/logo.png")
logo = tk.Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = tk.PhotoImage(file="E:/Weather APP in PYTHON/ImageS/box.png")
frame_myimage = tk.Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=tk.BOTTOM)

# Time
name = tk.Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = tk.Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
label1 = tk.Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#ADD8E6")
label1.place(x=120, y=400)

label2 = tk.Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#ADD8E6")
label2.place(x=250, y=400)

label3 = tk.Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#ADD8E6")
label3.place(x=430, y=400)

label4 = tk.Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#ADD8E6")
label4.place(x=650, y=400)

t = tk.Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = tk.Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
