import tkinter as tk
from functions import encrypt_to_morse,encrypt_to_plane

#Configuración de la pantalla
wroot = tk.Tk()
wroot.title("Conversor de código morse")
wroot.geometry("700x600")

#Configuración frame general

fr_general = tk.Frame(wroot,width=660, height=570,bg= "lightgrey") #"#f0f0f0"
fr_general.place(x=20,y=20)

fr_general.pack_propagate(0)
lbl_title = tk.Label(fr_general,text="TRADUCTOR MORSE",anchor = tk.W)

lbl_title.pack(side=tk.TOP)






wroot.mainloop()
