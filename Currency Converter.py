import tkinter as tk
from tkinter import messagebox

def real_time_currency_conversion():
    amount = float(Amount1_field.get())
    from_currency = variable1.get()
    to_currency = variable2.get()

    conversion_rate = 1.0

    if from_currency == "INR" and to_currency == "USD":
        conversion_rate = 0.014
    elif from_currency == "INR" and to_currency == "CAD":
        conversion_rate = 0.018
    elif from_currency == "INR" and to_currency == "CNY":
        conversion_rate = 0.089
    elif from_currency == "INR" and to_currency == "DKK":
        conversion_rate = 0.088
    elif from_currency == "INR" and to_currency == "EUR":
        conversion_rate = 0.012
    elif from_currency == "USD" and to_currency == "INR":
        conversion_rate = 72.16
    elif from_currency == "CAD" and to_currency == "INR":
        conversion_rate = 55.34
    elif from_currency == "CNY" and to_currency == "INR":
        conversion_rate = 11.51
    elif from_currency == "DKK" and to_currency == "INR":
        conversion_rate = 11.34
    elif from_currency == "EUR" and to_currency == "INR":
        conversion_rate = 78.44
    elif from_currency == "CAD" and to_currency == "CNY":
        conversion_rate = 5.97
    elif from_currency == "CAD" and to_currency == "DKK":
        conversion_rate = 5.64
    elif from_currency == "CAD" and to_currency == "EUR":
        conversion_rate = 0.85
    elif from_currency == "CNY" and to_currency == "CAD":
        conversion_rate = 0.17
    elif from_currency == "DKK" and to_currency == "CAD":
        conversion_rate = 0.18
    elif from_currency == "EUR" and to_currency == "CAD":
        conversion_rate = 1.18
    elif from_currency == "CNY" and to_currency == "DKK":
        conversion_rate = 0.94
    elif from_currency == "CNY" and to_currency == "EUR":
        conversion_rate = 0.14
    elif from_currency == "DKK" and to_currency == "CNY":
        conversion_rate = 1.06
    elif from_currency == "DKK" and to_currency == "EUR":
        conversion_rate = 0.15
    elif from_currency == "EUR" and to_currency == "CNY":
        conversion_rate = 7.20
    elif from_currency == "EUR" and to_currency == "DKK":
        conversion_rate = 6.80

    converted_amount = amount * conversion_rate
    Amount2_field.delete(0, tk.END)
    Amount2_field.insert(0, round(converted_amount, 4))

def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)

root = tk.Tk()
root.title("GUI : Currency Conversion")

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("currency")
variable2.set("currency")

Tops = tk.Frame(root, bg='#663300', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='     3rd Year Python Mini-Project :    Currency Converter  ', bg='#663300', fg='white')
headlabel.grid(row=1, column=0, sticky=tk.W)

CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

root.configure(background='#e6e5e5')
root.geometry("700x400")

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=tk.W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=tk.W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=tk.W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=tk.W)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=tk.E)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

FromCurrency_option.grid(row=3, column=0, ipadx=10, sticky=tk.E)
ToCurrency_option.grid(row=4, column=0, ipadx=10, sticky=tk.E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=28, sticky=tk.E)

button1 = tk.Button(root, font=('lato black', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="blue", fg="white", command=real_time_currency_conversion)
button1.grid(row=5, column=0)

button2 = tk.Button(root, font=('lato black', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="white", fg="red", command=clear_all)
button2.grid(row=9, column=0)

root.mainloop()
