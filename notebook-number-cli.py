#دفترچه تلفن: قابلیت اضافه کردن ، حذف کردن و ویرایش اطلاعات همچنین قابلیت سرچ کردن با استفاده از نام و نمایش اطلاعات به صورت مجزا

import json


class NootebookNumber:
    def __init__(self,file_name = 'number.json'):
        self.file_name = file_name
        self.notebook = {}
        self.load_from_file()

    def show_menu(self):
        print("-------- Phone Notebook Menu --------")
        print("1. Add new number")
        print("2. Delete number")
        print("3. Edit number")
        print("4. Show information of ONE person")
        print("5. Show ALL contacts")
        print("6. Exit")

    def get_choice(self):
        choice =int( input("Well, What will you do?(1, 2, 3, 4, 5)..."))

        if choice == 1:
            self.add_number()

        elif choice == 2:
            self.delet_number()

        elif choice == 3:
            self.edit()

        elif choice == 4:
            self.show_information_one()

        elif choice == 5:
            self.show_all()

        elif choice == 6:
            print("Have a nice day!")
            exit()
        
        else:
            print("Invalid choice!")

    def add_number(self):
        fname = input("Full name(first name and last name): ")
        number = input("Number: ")
        address = input("Address: ")
        about = input("About: ")

        self.notebook[fname] = {
            "number": number,
            "address": address,
            "about": about
        }
        self.save_to_file()
        print("Added successfully.")

    def delet_number(self):
        name = input("Enter the name you want to delete it: ")
        if name in self.notebook:
            self.notebook.pop(name)
            self.save_to_file()
            print("it's deleted.")
        
        else:
            print("Name NOT found.")

    def edit(self):
        name = input("Enter the name you want to edit it: ")

        if name in self.notebook:
            print("Enter the new information(leave empty to keep old value):")

            old = self.notebook[name]

            new_number = input("New number: ") or old["number"]
            new_address = input("New address: ") or old["address"]
            new_about = input("New about: ") or old["about"]

            self.notebook[name] = {
            "number": new_number,
            "address": new_address,
            "about": new_about
        }
            self.save_to_file()
            print("Updated!")

        else:
            print("Name NOT found. Add it instead.")
            self.add_number()

    def show_information_one(self):
        name = input("Enter the name to show info: ")
        if name in self.notebook:
            info = self.notebook[name]
            print(f"\nName: {name}")
            print(f"Number: {info["number"]}")
            print(f"Address: {info["address"]}")
            print(f"About: {info["about"]}")
        else:
            print("Name NOT found.")

    def show_all(self):
        if not self.notebook:
            print("No contents saved.")
            return
        
        print("-------- All contents --------")
        for index (name, info) in enumerate(self.notebook.items(), start=1):
            print(f"{index}. {name} * {info["number"]}", sep=',')
            print("-"*20)

    def save_to_file(self):
        with open(self.file_name, "w") as file:
            json.dump(self.notebook, file, indent=4)
            print("Saved!!")

    def load_from_file(self):
        try:
            with open (self.file_name, 'r') as file:
                self.notebook = json.load(file)
        
        except FileNotFoundError:
            self.notebook = {}

#اجرای برنامه
app = NootebookNumber()
while True:
    app.show_menu()
    app.get_choice()

