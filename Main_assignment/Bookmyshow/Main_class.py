from Bookmyshow.Admin import Admin
from Bookmyshow.Excel import ExcelUtils
from Bookmyshow.User_class import User

while True:
    user_input = int(input("******Welcome to BookMyShow******* \n1. Login \n2. Register new account\n3.Exit\n"))
    if user_input == 1:
        admin_object = Admin()
        result = admin_object.admin_login()
        while True:
            if result == "Login Successful":
                user_input = int(input("1.Admin Login:\n******Welcome Admin*******\n"
                                       "1. Add New Movie Info\n2. Edit Movie Info\n3. Delete Movies\n4.Logout\n"))
            if user_input == 1:
                admin_object.add_movie()
            if user_input == 2:
                admin_object.EditMovie()
            if user_input == 3:
                admin_object.deleteMovie()
            if user_input == 4:
                break