"""
This module contains access permission
"""

__all__ = ["access"]


import pickle
from cryptography.fernet import Fernet


def access(user_name, password_entered):
    with open("users_data.pkl", 'rb') as user_data:
        user_pass = pickle.load(user_data)
        for user, password in user_pass.items():
            key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
            f = Fernet(key)
            passcode = (f.decrypt(password)).decode('utf-8')

            if user == user_name and passcode == password_entered:
                return True
        else:
            return False
