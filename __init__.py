import tkinter as tk
from time import strftime as time

relogio = tk.Label(text=time("%H:%M:%S"), font="Helvetica 120 bold")
relogio.pack()

def relogio_digital():
    agora = time("%H:%M:%S")
    if relogio['text'] != agora:
        relogio['text'] = agora
    relogio.after(100,tictac)

relogio_digital()
relogio.mainloop()
