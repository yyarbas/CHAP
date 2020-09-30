#!/usr/bin/env python3

import xmlrpc.client
import hashlib
import time
from getpass import getpass

#Initialize Server at specified Port
server = xmlrpc.client.ServerProxy('http://localhost:8000')

#Run in Loop for better usability of the program
while True:
	
	#clears the console
	print('\033[H\033[J')

	#Menu
	print(50*'-')
	print('MENU')
	print(50*'-')
	print('1. LogIn')
	print('2. Exit')
	print(50*'-')

	
	print('Enter a Number')
	user_input = input('Your choice: ')
	if user_input == '1':
		print("LogIn")

		#Input of User-Credentials
		username = input("Username:")
		password = str(getpass())
	
		#Request of Token for the Username
		token = server.authenticate(username)
		password_token = password + token

		#hash password and token(random nunmber)
		password_token_hash = hashlib.md5(password_token.encode('utf-8')).hexdigest()
		authorized_successful = server.authorize(username, password_token_hash)

		#If the autorization is successful open the premium functions menu
		if authorized_successful == 1:
			
				print('authorized for premium functions')
				time.sleep(3)

				
				while(user_input == '1'):
					print('\033[H\033[J')
					print('1. Pow')
					print('2. Divide')
					print('3. LogOut')

					print('Enter a Number')
					premium_function_input = input('Your Choice: ')

					if premium_function_input == '1':
						first_entry = int(input('First Number: '))
						second_entry = int(input('Second Number: '))
						result = server.pow(first_entry,second_entry)
						print('The result is ' + str(result))
						time.sleep(3)

					elif premium_function_input == '2':
						first_entry = int(input('First Number: '))
						second_entry = int(input('Second Number: '))
						result = server.div(first_entry,second_entry)
						print('The result is ' + str(result))
						time.sleep(3)

					elif premium_function_input == '3':
						break
					
					print('\033[H\033[J')
					print('Do want to do another Operation?')
					print('1.Yes')
					print('2.No')
					print('Enter a Number')
					print('Your Choice: ')
					user_input = input()
			

		if authorized_successful != 1:
			print('Username/Password is invalid!')
			print('Access denied!')
			time.sleep(5)
	
	#Exit the program 
	elif user_input == '2':
		exit()
 
	else:
		print('\033[H\033[J') 
		print('\033[4m' + 'Invalid choice!' + '\033[0m' )
		print('Try Again!')
		time.sleep(5)
		
