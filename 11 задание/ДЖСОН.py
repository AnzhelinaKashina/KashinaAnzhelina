import json
import requests

from tkinter import *
from tkinter import ttk
def show_message():
    otv = username.get()  # получаем введенный текст
    url = f"https://api.github.com/users/{otv}"
    # делаем запрос и возвращаем json
    user_data = requests.get(url).json()
    # довольно распечатать данные JSON
    with open("fff.json", "a") as f:
        print('Company:', user_data['company'],file=f)
        print('created_at:', user_data['created_at'],file=f)
        print('email:', user_data['email'], file=f)
        print('id:', user_data['id'],file=f)
        print('name:', user_data['name'],file=f)
        print('url:', user_data['url'],file=f)

root = Tk()
root.title("JJSSOONN")
root.geometry("450x400")

label = ttk.Label(text='Ввведите название профиля на GitHub и нажмите на кнопку', foreground="#01579B",
                   background="#B3E5FC")
label.pack(anchor='center', padx=6, pady=6)
username = ttk.Entry()
username.pack(anchor='center', padx=6, pady=6)

btn = ttk.Button(text="Click",command=show_message)
btn.pack(anchor='center', ipadx=10, ipady=5)
label= ttk.Label(text='Нажали на кнопку? Закрывайте это окно', foreground="#02939B",
                  background="violet")
label.pack(anchor='center', padx=6, pady=6)

root.mainloop()