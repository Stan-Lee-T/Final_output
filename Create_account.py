import tkinter as tk
import sqlite3
#Tayoto
class account_registration:
    def __init__(self):
        self.Access = None
        self.save_button = None
        self.exit_button = None
        self.main_frame = None
        self.content_frame = None

    def create_account(self):
        self.content_frame = tk.Frame(bg="gray")
        self.content_frame.pack(expand=True, fill="both")

    def content(self):
        self.main_frame = tk.LabelFrame(self.content_frame, width=900, height=500, relief="raised", borderwidth=10, bg="#CDCDCD", text="R E G I S T E R", font=("arial", 30, "bold"))
        self.main_frame.place(x=500, y=250)


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

    def exit(self):
        exit()

    def save(self):
        con = sqlite3.connect("C:\\Users\\Jeff\\PycharmProjects\\FinalOutput\\register_account.db")
        query = "INSERT INTO registered (username, password) VALUES ('" + self.username_entry.get() + "', '" + self.password_entry.get() + "')"
        con.execute(query)
        con.commit()
        con.close()
        self.Access = tk.Label(self.main_frame, text="Saved!", font=("arial", 20), bg="#CDCDCD")
        self.Access.place(y=325, x=50)

    def buttons(self):
        self.exit_button = tk.Button(self.main_frame, width=15, height=2, text="C A N C E L", font=("arial", 12, "bold"), command=self.exit, bg="#C5C6C7", relief="raised", borderwidth=10)
        self.exit_button.place(y=350, x=650)
        self.save_button = tk.Button(self.main_frame, width=15, height=2, text="R E G I S T E R", font=("arial", 12, "bold"), command=self.save, bg="#C5C6C7", relief="raised", borderwidth=10)
        self.save_button.place(y=350, x=425)


