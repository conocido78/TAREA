import tkinter as tk
from tkinter import messagebox

def hacePot():
    a = int(cajaA.get())
    b = int(cajaB.get())
    r = a
    i = 1
    while i < b:
        r = r * a
        i = i + 1
    messagebox.showinfo("Resu", f"{a} multiplicado {b} veces es: {r}")

ventana = tk.Tk()
ventana.title("resultado")

txtA = tk.Label(ventana, text="a:")
txtA.pack()
cajaA = tk.Entry(ventana)
cajaA.pack()

txtB = tk.Label(ventana, text="b:")
txtB.pack()
cajaB = tk.Entry(ventana)
cajaB.pack()

boton = tk.Button(ventana, text="resultado", command=hacePot)
boton.pack()

ventana.mainloop()
