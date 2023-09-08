import customtkinter as ctk
# import tkinter as tk
from tkinter import *

# app config
ctk.set_default_color_theme ("green")
ctk.set_appearance_mode ("light")

# root window
root = ctk.CTk ()
root.geometry("600x520")
root.title ("Helium Notes")

framex, framey = 590, 510
widthx, widthy = 170, 35
c_radius, pad_x, pad_y = 10, 10, 10
mid = 0.5

# frame
frame = ctk.CTkFrame (master = root, width = framex, height = framey, corner_radius = c_radius)

mode_name = StringVar (value = ctk.get_appearance_mode())

def change_bg ():

    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
        mode_name.set("Dark")
    else:
        ctk.set_appearance_mode("Dark")
        mode_name.set("Light")




switch_01 = ctk.CTkSwitch (master = frame, textvariable = mode_name, switch_width = 40, command = change_bg)

def dissable ():
    if switch_02.get() == 1:
        switch_01.configure(state = "disabled")

    if switch_02.get() == 0:
        switch_01.configure(state = "normal")



switch_02 = ctk.CTkSwitch (master = frame, text = "Dissable Mode", switch_width = 40, command = dissable)




frame.pack(padx=pad_x, pady=pad_y)
switch_01.place(relx=mid, rely=0.3, anchor = CENTER)
switch_02.place(relx=mid, rely=0.5, anchor = CENTER)
if __name__ == '__main__':
    root.mainloop()

