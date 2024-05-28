import tkinter as tk
from tkinter import *
from tkinter import ttk
# from PIL import Image, ImageTk
import sqlite3

con = sqlite3.connect("C:\\Users\\Jeff\\PycharmProjects\\FinalOutput\\employee_personal_info.db")
class employee_personal_info():

    def create_canvas(self, x, y):
        self.canvas = tk.Canvas()
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_container = tk.Frame(self.canvas)

        self.frame1 = tk.Frame(self.frame_container, width=995, height=1500, bg='gray')
        self.frame1.pack()

        self.frame_container.update_idletasks()
        self.canvas.create_window(0, 0, window=self.frame_container, anchor='nw')
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        return self.frame_container

    def create_frames(self, frame_container, x, y, bg_color, width, height):
        self.frame2 = tk.Frame(frame_container, width = width, height = height, bg = bg_color)
        self.frame2.place (x=x, y=y)
        return self.frame2

    def label1(self, frame_container,x, y, label_name):
        self.label_name = label_name
        self.lbl = tk.Label(frame_container,text=label_name, fg = 'black', bg = 'light blue',font =('Calibri', 12))
        self.lbl.place(x=x, y=y)
        return self.lbl

    def label2(self, frame_container,x, y, label_name,font_size, font_style):
        self.label_name = label_name
        self.lbl = tk.Label(frame_container,text=label_name, fg = 'beige', bg = 'light blue',font =('Arial', font_size, font_style))
        self.lbl.place(x=x, y=y)
        return self.lbl

    def label3(self, frame_container,x, y, label_name,width_value,height_value,font_size,font_style):
        self.label_name = label_name
        self.lbl = tk.Label(frame_container,text=label_name, width=width_value, height=height_value, fg = 'black', bg = 'gray',font =('Arial', font_size, font_style))
        self.lbl.place(x=x, y=y)
        return self.lbl

    def label4(self, frame_container,x, y, label_name):
        self.label_name = label_name
        self.lbl = tk.Label(frame_container, text=label_name, fg='black', bg='light blue', font=('Arial', 12, 'bold'))
        self.lbl.place(x=x, y=y)
        return self.lbl

    def textbox1(self, frame_container,x, y,width_value):
        self.textbox = Entry(frame_container,width=width_value, fg = 'black', border = 1, font =('Arial', 12))
        self.textbox.place(x=x, y=y)
        return self.textbox

    # def picture(self, frame_container,x, y, length, width, image_location):
    #     self.length = length
    #     self.width = width
    #     self.image_location = image_location
    #     self.image = Image.open(image_location)
    #     self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
    #     self.lbl = Label(frame_container,image=self.bck_pic)
    #     self.lbl.place(x=x, y=y)
    #     return self.lbl

    def create_button(self, frame_container,command, x, y, button_name, bg, width_value, height_value, font_size):
        self.button_name = button_name
        self.bg = bg
        self.button = Button(frame_container,command=command, text=button_name, width=width_value, height=height_value, fg = 'black', bg = bg, font =('Arial', font_size))
        self.button.place(x=x, y=y)
        return self.button

    def create_combobox(self, frame_container,x, y, values):
        self.combobox = ttk.Combobox(frame_container, values=values, width=12, font =('Arial', 12))
        self.combobox.place(x=x, y=y)
        return self.combobox
