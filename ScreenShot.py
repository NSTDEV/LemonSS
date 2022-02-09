import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import pyautogui
from webbrowser import *


lastClickX = 0
lastClickY = 0


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + vn.winfo_x(), event.y - lastClickY + vn.winfo_y()
    vn.geometry("+%s+%s" % (x , y))


def ssWidget():
	botonCaptura = Button(vn, text="Capturar", width=10, font=("Rainyhearts", 15), bg="#fae38c", fg="#5b4a09", borderwidth=5, command=capturar)
	botonCaptura.pack(side=LEFT, padx=5)
	
	closeButton = Button(vn, text="x", width=2, bg="#fae38c", highlightbackground="#5b4a09", borderwidth=5, command=vn.destroy)
	closeButton.pack(side=RIGHT, pady=3, padx=5)
	

def capturar():
	vn.withdraw()
	capturar = pyautogui.screenshot()
	direccion = filedialog.asksaveasfilename(defaultextension=".png",filetypes=(("Archivo Png", "*.png"),("Todos los archivos", "*.*")))
	capturar.save(direccion)
	messagebox.showinfo("¡Genial!", "Captura Guardada (ಥ 3 ಥ)")
	vn.deiconify()

vn = tk.Tk()
vn.title("LemonSS")
vn.attributes('-toolwindow', 'True')
vn.config(bg="#fae38c")
vn.attributes("-alpha", 0.85)
vn.attributes("-topmost", True)
vn.geometry("170x48")
vn.overrideredirect(True)
vn.bind('<Button-1>', SaveLastClickPos)
vn.bind('<B1-Motion>', Dragging)

ssWidget()

vn.mainloop()