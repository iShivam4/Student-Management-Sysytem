"""
This file is used to add users and password to the database
"""


import pickle
from getpass import getpass
from cryptography.fernet import Fernet

try:
    with open("users_data.pkl", 'rb') as user_data:
        user_pass = pickle.load(user_data)

except FileNotFoundError:
    # creating a new dict if file is doesn't exist
    user_pass = dict()

add = False
command = input("Do you want to add user --> ")

if command in ["Yes", 'yes', "Y", 'y']:
    add = True
else:
    add = False

while add:
    username = input("Enter user name: ")
    password = getpass("Enter Password")
    # password = input("Enter Password: ")
    # converting password to bytes
    password = bytes(password, 'utf-8')
    # generating key for encryption
    key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
    f = Fernet(key)
    passcode = f.encrypt(password)

    if username in user_pass:
        print("User already existed")
        break
    else:
        user_pass[username] = passcode

    add = False

with open("users_data.pkl", 'wb') as users:
    pickle.dump(user_pass, users)

print(user_pass)

close = input("Press Q to exit")
