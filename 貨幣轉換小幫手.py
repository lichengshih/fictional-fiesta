from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import requests
import datetime as dt

class CurrencyConverter:

    def __init__(self, url):
        self.url = 'https://api.exchangerate-api.com/v4/latest/USD'
        self.response = requests.get(url)
        self.data = self.response.json()
        self.rates = self.data.get('rates')

    def convert(self, amount, base_currency, quoted_currency):
        if base_currency != 'USD':
            amount = amount/self.rates[base_currency]

        amount = round(amount*self.rates[quoted_currency], 2)
        amount = '{:,}'.format(amount)
        return amount

class Main(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('貨幣轉換小幫手')
        self.geometry('400x400')
        self.CurrencyConverter = converter

        self.title = Label(self, text='貨幣轉換小幫手',font=('time new roman', 20))
        self.title.place(x=200, y=35, anchor='center')

        self.amount = Label(self, text='請輸入金額: ')
        self.amount.place(x=200, y=80, anchor='center')

        self.amount_entry = Entry(self)
        self.amount_entry.place(x=200, y=110, anchor='center')

        self.base_currency_label = Label(self, text='從： ')
        self.base_currency_label.place(x=200, y=140, anchor='center')

        self.destination_currency_label = Label(self, text='到： ')
        self.destination_currency_label.place(x=200, y=200, anchor='center')

        self.currency_variable1 = StringVar(self)
        self.currency_variable2 = StringVar(self)
        self.currency_variable1.set('USD')
        self.currency_variable2.set('TWD')

        self.currency_combobox1 = ttk.Combobox(self, textvariable=self.currency_variable1, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
        self.currency_combobox1.place(x=200, y=170, anchor='center')

        self.currency_combobox2 = ttk.Combobox(self, textvariable=self.currency_variable2, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
        self.currency_combobox2.place(x=200, y=230, anchor='center')

        self.convert_button = Button(self, text='轉換', command=self.processed)
        self.convert_button.place(x=170, y=270, anchor='center')

        self.clear_button = Button(self, text='清除', command=self.clear)
        self.clear_button.place(x=230, y=270, anchor='center')

        self.final_result = Label(self, text='',)
        self.final_result.place(x=200, y=310, anchor='center')
        
        self.date_label = Label(self, text=f'目前時間為: {dt.datetime.now():%Y 年 %m 月 %d 日 %H 時 %M 分}')
        self.date_label.place(x=0, y=400, anchor='sw')

    def clear(self):
        clear_entry = self.amount_entry.delete(0, END)
        clear_result = self.final_result.config(text='')
        return clear_entry, clear_result

    def processed(self):
        try:
            given_amount = float(self.amount_entry.get())
            given_base_currency = self.currency_variable1.get()
            given_quoted_currency = self.currency_variable2.get()
            converted_amount = self.CurrencyConverter.convert(given_amount, given_base_currency, given_quoted_currency)
            given_amount = '{:,}'.format(given_amount)

            self.final_result.config(text=f'{given_amount} {given_base_currency} = {converted_amount} {given_quoted_currency}')

        except ValueError:
            convert_error = messagebox.showwarning('警告！', '請輸入正確資訊 (限數字)！')
            return convert_error

if __name__ == '__main__':
    converter = CurrencyConverter('https://api.exchangerate-api.com/v4/latest/USD')
    Main(converter)
    mainloop()