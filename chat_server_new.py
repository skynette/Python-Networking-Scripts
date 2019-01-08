import socket
import time

host = "127.0.0.1"
port = 5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quitting = False
print("Server Started ")

while not quitting:
	try:
		data, address = s.recvfrom(1024)
		if "quit" in data.encode(utf-8):
			quitting = True
		if address not in clients:
			clients.append(address)

		print time.ctime(time.time()) + str(address) + ": :" + data.decode(utf+8)
		for client in clients:
			s.sendto(data, client)
	except:
		pass		
s.close()