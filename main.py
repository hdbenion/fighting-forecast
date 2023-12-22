'''
Main file to handle the user interface and interaction.
'''
from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu
from admin import Admin, AdminMenu
from user import User, UserMenu
class BoxingPredictionChallenge:
    def __init__(self, master):
        self.master = master
        master.title("Boxing Prediction Challenge")
        self.label = Label(master, text="Welcome to Boxing Prediction Challenge!")
        self.label.pack()
        self.admin_button = Button(master, text="Admin Login", command=self.admin_login)
        self.admin_button.pack()
        self.user_button = Button(master, text="User Login", command=self.user_login)
        self.user_button.pack()
    def admin_login(self):
        # Logic to handle admin login
        admin = Admin()
        # Prompt the admin for username and password
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        # Validate the admin credentials
        if admin.validate_credentials(username, password):
            # Proceed with admin actions
            admin_menu = AdminMenu(admin)
            admin_menu.show_menu()
        else:
            print("Invalid admin credentials")
    def user_login(self):
        # Logic to handle user login
        user = User()
        # Prompt the user for username and password
        username = input("Enter user username: ")
        password = input("Enter user password: ")
        # Validate the user credentials
        if user.validate_credentials(username, password):
            # Proceed with user actions
            user_menu = UserMenu(user)
            user_menu.show_menu()
        else:
            print("Invalid user credentials")
root = Tk()
boxing_challenge = BoxingPredictionChallenge(root)
root.mainloop()