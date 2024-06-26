import tkinter as tk
import Create_account
import sqlite3

root = tk.Tk()

class GUI:
    def __init__(self):
        self.create_account_button = None
        self.password_entry = None
        self.username_entry = None
        self.password_label = None
        self.username_label = None
        self.login_button = None
        self.exit_button = None
        self.main_frame = None
        self.content_frame = tk.Frame(root, bg="gray")
        self.content_frame.pack(fill="both", expand=True)

    def Exit(self):
        exit()

    def login(self):
        print("Login")

    def create_account(self):
        account_registration = Create_account.account_registration()
        account_registration.create_account()
        account_registration.content()
        account_registration.buttons()
        account_registration.labels()
        account_registration.entries()
        self.content_frame.destroy()

    def frames(self):
        self.main_frame = tk.LabelFrame(self.content_frame, width=900, height=500, relief="raised", borderwidth=10, bg="#CDCDCD", text="L O G I N", font=("arial", 30, "bold"))
        self.main_frame.place(x=500, y=250)

    def buttons(self):
        self.exit_button = tk.Button(self.main_frame, width=15, height=2, text="C A N C E L", font=("arial", 12, "bold"), command=self.Exit, bg="#C5C6C7", relief="raised", borderwidth=10)
        self.exit_button.place(y=350, x=650)
        self.login_button = tk.Button(self.main_frame, width=15, height=2, text="L O G I N", font=("arial", 12, "bold"), command=self.login, bg="#C5C6C7", relief="raised", borderwidth=10)
        self.login_button.place(y=350, x=425)
        self.create_account_button = tk.Button(self.content_frame, width=30, height=2, text="C R E A T E  A N  A C C O U N T", font=("arial", 12, "bold"), command=self.create_account, bg="gray", relief="flat", borderwidth=0)
        self.create_account_button.place(y=750, x=1025)

    def labels(self):
        self.username_label = tk.Label(self.main_frame, text="Username", font=("arial", 20), bg="#CDCDCD")
        self.username_label.place(y=50, x=50)
        self.password_label = tk.Label(self.main_frame, text="Password", font=("arial", 20), bg="#CDCDCD")
        self.password_label.place(y=200, x=50)

    def entries(self):
        self.username_entry = tk.Entry(self.main_frame, width=50, font=("arial", 20))
        self.username_entry.place(y=85, x=50)
        self.password_entry = tk.Entry(self.main_frame, width=50, show="*", font=("arial", 20))
        self.password_entry.place(y=235, x=50)


GUI = GUI()
GUI.frames()
GUI.buttons()
GUI.labels()
GUI.entries()
root.attributes("-fullscreen", True)
root.mainloop()
