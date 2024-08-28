import requests
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Function to get the conversion rate from one currency to another

def get_conversion_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rates = data['rates']
        if to_currency in rates:
            return rates[to_currency]
        else:
            messagebox.showerror("Error", f"Conversion rate for {to_currency} not found.")
            return None
    else:
        messagebox.showerror("Error", "Failed to retrieve conversion rates.")
        return None

# Function to perform the conversion

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()
        
        if from_currency == "" or to_currency == "":
            messagebox.showerror("Error", "Please select both currencies.")
            return
        
        rate = get_conversion_rate(from_currency, to_currency)
        if rate is not None:
            converted_amount = amount * rate
            result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# Initialize the main window

root = Tk()
root.title("Currency Converter")

# Load and resize the background image

background_image = Image.open("pybg.jpg")
window_width, window_height = 1600, 800  # Set your desired window size
background_image = background_image.resize((window_width, window_height))
background_photo = ImageTk.PhotoImage(background_image)

# Create a Canvas widget to place the background image

canvas = Canvas(root, width=window_width, height=window_height)
canvas.pack(fill="both", expand=True)

# Display the background image on the Canvas

canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Frame for holding the widgets to make them visible over the background

frame = Frame(canvas, bg='white', padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Title label

title_label = Label(frame, text="Currency Converter", font=("Arial", 20, "bold"), bg='white', fg='#007BFF')
title_label.grid(row=0, columnspan=2, pady=10)

# Amount entry

amount_label = Label(frame, text="Amount:", font=("Arial", 12, "bold"), bg='white')
amount_label.grid(row=1, column=0, pady=10, sticky='e')
amount_entry = Entry(frame, font=("Arial", 12), width=15)
amount_entry.grid(row=1, column=1, pady=10, padx=10)

# From currency selection

from_currency_label = Label(frame, text="From:", font=("Arial", 12, "bold"), bg='white')
from_currency_label.grid(row=2, column=0, pady=10, sticky='e')
from_currency_combo = ttk.Combobox(frame, values=[
    "USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD",
    "NOK", "KRW", "TRY", "RUB", "ZAR", "BRL"
], font=("Arial", 12), width=13)
from_currency_combo.grid(row=2, column=1, pady=10, padx=10)

# To currency selection

to_currency_label = Label(frame, text="To:", font=("Arial", 12, "bold"), bg='white')
to_currency_label.grid(row=3, column=0, pady=10, sticky='e')
to_currency_combo = ttk.Combobox(frame, values=[
    "USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD",
    "NOK", "KRW", "TRY", "RUB", "ZAR", "BRL"
], font=("Arial", 12), width=13)
to_currency_combo.grid(row=3, column=1, pady=10, padx=10)

# Convert button

convert_button = Button(frame, text="Convert", command=convert_currency, font=("Arial", 12, "bold"), bg='#007BFF', fg='white', relief=RAISED)
convert_button.grid(row=4, columnspan=2, pady=20)

# Result label

result_label = Label(frame, text="", font=("Arial", 12, "bold"), bg='white')
result_label.grid(row=5, columnspan=2, pady=10)

root.mainloop()
