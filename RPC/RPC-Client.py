#!/usr/bin/env python3

import xmlrpc.client
import hashlib
from getpass import getpass

server = xmlrpc.client.ServerProxy('http://localhost:8000')

#Show Methods of running Server
print(server.system.listMethods())

print("LogIn")

username = input("Username:")
password = str(getpass())
	
token = server.auth(username)
print(token[0])
print(token[1])
password_token = password + token[0]
password_token_hash = hashlib.md5(password_token.encode('utf-8')).hexdigest()
if token[1] == password_token_hash:
	