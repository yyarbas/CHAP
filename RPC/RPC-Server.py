#!/usr/bin/env python3

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import json
import os

import random

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler,
							allow_none = True)
server.register_introspection_functions()

server.register_function(pow)

class MyFuncs:
    def div(self, x, y):
        return x // y

server.register_instance(MyFuncs())

def authenticate_user_function(username):
	import hashlib
	import random
	global random_number
	with open(os.path.join(sys.path[0], "userAccountData.json"), "r") as json_file:
		data = json.load(json_file)
		for account in data['accounts']:
			if account['username'] == username:
				random_number = str(random.randrange(1,9999))
				
				return  random_number

def authorize_user_funtion(username, password, password_token_hash_client):
	import hashlib
	import random
	with open(os.path.join(sys.path[0], "userAccountData.json"), "r") as json_file:
		data = json.load(json_file)
		for account in data['accounts']:
			if account['username'] == username:
				if account['password'] == password:
					password_token = password + random_number
					password_token_hash_server = hashlib.md5(password_token.encode('utf-8')).hexdigest()
					if password_token_hash_server ==  password_token_hash_client: 
						return  1
					else: 
						return 0


server.register_function(authenticate_user_function,'authenticate')
server.register_function(authorize_user_funtion,'authorize')


        
# Run the server's main loop
try:
    print('Starting Server..')
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting Server..')
