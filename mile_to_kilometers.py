from tkinter import *

def miles_to_km():
   miles = float(miles_input.get())
   km = round(miles * 1.609)
   km_result_label.config(text=f"km")

window = Tk()
window.title = "Miles To Kiometer Converter"

miles_input = Entry()
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=1)

km_result_label = Label(text="0")
km_result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=1, column=2)
