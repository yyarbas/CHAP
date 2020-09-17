#!/usr/bin/env python3

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import json

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

with open("C:\\Users\\yarbas\\Downloads\\userAccountData.json") as json_file:
    data = json.load(json_file)
    for p in data['accounts']:
         if p['username'] == 'XXusernameToCheckXX' and  p['password'] == 'XXpasswordToCheckXX'
        
# Run the server's main loop
server.serve_forever()
