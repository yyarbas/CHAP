#!/usr/bin/env python3

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

print("LogIn")
username = input("Username:")

password = input("Password:")

auth = s.auth(username)
print(auth)