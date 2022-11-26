# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:09:01 2022

@author: Bhanvi
"""

email = input("Enter Your Email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]
print(f"Your username is {username} & domain is {domain}")
