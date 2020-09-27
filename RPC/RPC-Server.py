#!/usr/bin/env python3

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import json

import random

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

server.register_function(pow)

class MyFuncs:
    def div(self, x, y):
        return x // y

server.register_instance(MyFuncs())

def authenticate_user_function(username):
	import hashlib
	import random
	with open('C:\\Users\\yakup\\source\\repos\\yyarbas\\CHAP\\RPC\\userAccountData.json') as json_file:
		data = json.load(json_file)
		for account in data['accounts']:
			if account['username'] == username:
				random_number = str(random.randrange(1,9999))
				password = account['password']
				password_token = password + random_number
				password_token_hash = hashlib.md5(password_token.encode('utf-8')).hexdigest()
				return  random_number , password_token_hash
            
server.register_function(authenticate_user_function,'auth')


        
# Run the server's main loop
try:
    print('Starting Server..')
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting Server..')
