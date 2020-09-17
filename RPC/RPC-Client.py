#!/usr/bin/env python3

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

print("LogIn")
print("Username: ")
username = input()
print("Password: ")
password = input()
