import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receiving (name, sock):
	while not shutdown:
		try:
			tLock.aquire()
			while True:
				data, address = sock.recvfrom(1024)
				print (str(data))
		except:
			pass
		finally:
			# tLock.release()
			pass

host = "127.0.0.1"
port = 0

server = ("127.0.0.1", 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receiving, args=("recvThread", s))
rT.start()
alias = str(input("Name: "))
message = input(alias + "..> ")

while message != "q":
	if message != "":
		s.sendto(alias + ": " + message.encode(utf-8), server)
		tLock.aquire()
		message = input (alias + "..> ")
		tLock.release()
		time.sleep(0.5)

shutdown = True
rT.join()		
s.close()




