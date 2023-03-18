import tkinter as tk
import requests
import time
from PIL import ImageTk, Image

def getWeather(canvas):
    city = textfield.get()
    textfield.config(fg = "brown")
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    
    if condition == 'Thunderstorm':
        condition = 'Gök Gürültülü Fırtına'
    elif condition == 'Drizzle':
        condition = 'Çisenti'
    elif condition == 'Rain':
        condition = 'Yağmurlu'
    elif condition == 'Snow':
        condition = 'Karlı'
    elif condition == 'Clear':
        condition = 'Açık'
    elif condition == 'Clouds':
        condition = 'Bulutlu'
    else:
        condition = 'Bilinmeyen Durum'
    
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Maksimum Sıcaklık: " + str(max_temp) + "\n" + "Minimum Sıcaklık: " + str(min_temp) + "\n" + "Basınç: " + str(pressure) + "\n" + "Nem: " + str(humidity) + "\n" + "Rüzgar Hızı: " + str(wind) + "\n" + "Gün Doğumu: " + sunrise + "\n" + "Gün Batımı: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("800x600")
canvas.title("Hava Durumu")

img = Image.open("eren.jpg")
img = img.resize((800, 600), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(img)
background_label = tk.Label(canvas, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

f = ("Calisto MT Kalın",15,"bold")
t = ("Calisto MT Kalın",35,"bold")
textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.config(fg='brown')
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.config(fg='brown')
label2.pack()

canvas.mainloop()

