import requests
from pprint import pprint
from tkinter import *



window = Tk()
# Configuration
window.geometry("1000x500")
window.title("Weather Application")

def get_weather():
    city_name = en1.get()
    api_key = "5f2554b9b9d6a09612f025876fd9634c"

    api_link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(api_link)
    data = response.json()
    pprint(data)

    # estekhraj etelawt bedast omade az darkhasti ke be website zadim
    condition = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    temp_ = int(data["main"]["temp"] - 273.15)
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    lbl1_under.configure(text=wind, bg="yellow", fg="black")

en1 = Entry(window, font=("arial", 25), width=20, bd=5)
en1.place(x=100, y=100)

lbl1 = Label(window, text="wind", font=("arial", 25))
lbl1.place(x=100, y=200)

lbl1_under = Label(window, text="....", font=("arial", 25))
lbl1_under.place(x=100, y=250)

btn1 = Button(window, text="Search", command=get_weather, width=20, font=("arial", 25))
btn1.place(x= 400, y=100)


window.mainloop()



















