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


#Configuración frame dividio en tres

fr_division_0 = tk.Frame(fr_general,width=250, height=570,bg= "grey")
fr_division_0.place(x=25,y=25)

fr_division_1 = tk.Frame(fr_general,width=76, height=570,bg= "blue")
fr_division_1.place(x=291,y=25)

fr_division_2 = tk.Frame(fr_general,width=250, height=570,bg= "red")
fr_division_2.place(x=385,y=25)




wroot.mainloop()
