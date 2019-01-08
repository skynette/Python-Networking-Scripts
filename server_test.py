from socket import * # get socket constructor and constants

myHost = '' # '' = all available interfaces on host
myPort = 50007 # listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM) # make a TCP socket object
sockobj.bind((myHost, myPort)) # bind it to server port number
sockobj.listen(5) # listen, allow 5 pending connects
print ("[+] Server Started ")
while True: # listen until process killed
	connection, address = sockobj.accept() # wait for next client connect
	print('[+] New connection from', address) # connection is a new socket

	while True:
		data = connection.recv(1024) # read next line on client socket
		if not data: break # send a reply line to the client
		message =("message sent to client ")
		connection.send(message.encode("utf-8") + data) # until eof when socket closed
	connection.close()