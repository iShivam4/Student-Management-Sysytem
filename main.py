import csv
import os
from getpass import getpass
import store_load_data
from login import access


def clear():
    os.system('cls')


if __name__ == "__main__":

    loop1 = True

    while loop1:
        clear()
        print("Student Management System")
        print("1. Teacher")
        print("2. Students")

        try:
            role = int(input("Enter number: "))
            if role == 1:
                user = input("Enter user name-->")
                password = getpass("Enter password-->")
                check = access(user, password)
                if check:
                    loop1 = False
                    print("1. Enter Student Result")
                    print("2. Display Result")
                    print("3. Search Student Roll number")
                    category = int(input("Enter option number: "))

                    if category == 1:
                        loop3 = True
                        while loop3:
                            store_load_data.storeData()
                            take = input("\nDo you want to add more.(Yes/No or Y/N)-->")
                            if take in ['Y', 'y', 'Yes', "yes"]:
                                continue
                            else:
                                loop3 = False
                                close = input("\nPress Q to exit: ")

                    elif category == 2:
                        roll_no = input("Enter Roll no: ")
                        store_load_data.loadData(roll_no)
                        close = input("\nPress Q to exit: ")

                    elif category == 3:
                        name = input("Enter Name: ")
                        with open("Data.csv", 'r') as data:
                            reader = csv.DictReader(data)
                            for student in reader:
                                if student['Name'].upper() == name.upper():
                                    print("Student Name : ", student['Name'])
                                    close = input("\nPress Q to exit: ")
                            else:
                                print("Data not found")
                                close = input("\nPress Q to exit: ")
                                exit()
                            close = input("\nPress Q to exit: ")

                    else:
                        print("Incorrect option")
                        close = input("\nPress Q to exit: ")
                        exit()

                else:
                    print("Incorrect credentials entered.")
                    continue

            elif role == 2:
                print("1. Display result")
                print("2. Search role number")
                category = int(input("Enter option: "))
                if category == 1:
                    name = input("Enter name: ")
                    store_load_data.loadData(name)
                    loop1 = False
                    close = input("\nPress Q to exit: ")

                elif category == 2:
                    roll_no = input("Enter roll number: ")
                    store_load_data.loadData(roll_no)
                    loop1 = False
                    close = input("\nPress Q to exit: ")

            else:
                print("Incorrect number entered")
                close = input("\nPress any key to enter again: ")
                continue

        except ValueError:
            print("Incorrect number entered")
            print("Try again")
            close = input("\nPress any key to enter again: ")
            continue
