import tkinter as tk 
from tkinter import ttk
import requests
from PIL import ImageTk, Image
from urllib.request import urlopen


api_key = "YOUR_API KEY"  #9103920ecddaa42189025de42f3ae39c
base_url = "http://api.openweathermap.org/data/2.5/weather?"
window = tk.Tk()
window.geometry("700x600")
window.title("Weather Report By City ")
frame =tk.Frame(master=window,background="black")

def not_found():
    error_lable["text"]="Not a Valid City Name !"
    l1["text"]="--"
    l2["text"]="--"
    l3["text"]="--"
    l4["text"]="--"
    l5["text"]="--"
 
def found(temp,pressure, humidity, weather,city_name,icon):
     error_lable["text"]=""
     l1["text"]=str(temp) + " °C"
     l2["text"]=str(pressure) +" Pa"
     l3["text"]=str(humidity) + " %"
     l4["text"]=weather.upper() 
     l5["text"]=city_name.upper() 
     URL = f"https://openweathermap.org/img/wn/{icon}@2x.png"
     u = urlopen(URL)
     raw_data = u.read()
     u.close()
     photo = ImageTk.PhotoImage(data=raw_data)
     im = tk.Label(image=photo,bg="#B4EBFE")
     im.image = photo
     im.grid(row=7, column=3)



def get_city():
        try:
            temp,pressure, humidity, weather,city_name,icon =result()
        except :
             error_lable["text"]="Please Check Your Internet !"       
    
        if  "0" in [temp,pressure, humidity, weather,city_name,icon]:
            not_found()
        else:
            found(temp,pressure, humidity, weather, city_name,icon)
                

def clean():
    tk.Label(text=entry.delete(0, tk.END) )

def result():
    city_name = entry.get()
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid=9103920ecddaa42189025de42f3ae39c&q={city_name}")
    x = response.json()
    
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        tem = current_temperature-273.15
        temp= round(tem,1)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        icon =x['weather'][0]['icon']
        print(temp ,current_pressure, current_humidity, weather_description,icon)
        return  temp,current_pressure, current_humidity, weather_description, city_name,icon
        
    else:
        temp,current_pressure, current_humidity, weather_description,city_name,icon =['0','0','0','0','0','0']
        return temp,current_pressure, current_humidity, weather_description,city_name,icon


# Fields-- Headings------
tem = ttk.Label(window,text="Temperature :", font=('Helvetica 15')).grid(row=1, column=0, sticky=tk.E)
pre = ttk.Label(window,text="Pressure :", font=('Helvetica 15')).grid(row=3, column=0, sticky=tk.E)
humi = ttk.Label(window,text="Humidity :", font=('Helvetica 15')).grid(row=5, column=0, sticky=tk.E)
weat = ttk.Label(window,text="Weather :", font=('Helvetica 15')).grid(row=7, column=0, sticky=tk.E)
city = ttk.Label(window,text="City :", font=('Helvetica 15')).grid(row=10, column=0, sticky=tk.E)
#-----------


#lables-----Backend-----
error_lable= tk.Label(font=('Helvetica 17'))
l1=ttk.Label( font=('Helvetica 17'))
l2=ttk.Label(font=('Helvetica 17'))
l3=ttk.Label(font=('Helvetica 17'))
l4=ttk.Label(font=('Helvetica 17'))
l5=ttk.Label(font=('Helvetica 17'))


#-----Placement of result-----
error_lable.grid(row=44, column=2,sticky=tk.E)
l1.grid(row=1, column=2, sticky=tk.E)
l2.grid(row=3, column=2, sticky=tk.E)
l3.grid(row=5, column=2, sticky=tk.E)
l4.grid(row=7, column=2, sticky=tk.E)
l5.grid(row=10, column=2, sticky=tk.E)

#main Headind
lable=ttk.Label(window,text="Enter Your City Name : ", font=('Helvetica 15')).place(relx=.19, rely= .45,anchor="center")

#city field
entry = tk.Entry(width=40 , bg="white", fg="black")
entry.place(relx=.5, rely=.5 ,anchor="center")


# Buttons
button=ttk.Button(window,text='Show', command=get_city).place(relx=.3, rely= .6,anchor="center")
clear=ttk.Button(window,text='Clear', command=clean).place(relx=.5, rely= .6,anchor="center")
close=ttk.Button(window,text='Close', command=window.destroy).place(relx=.7, rely= .6,anchor="center")


window.mainloop()
