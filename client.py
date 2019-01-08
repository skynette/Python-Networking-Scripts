from socket import *
import sys

def main():

	host = "127.0.0.1"
	port = 5000

	# s =socket.socket()
	s = socket(AF_INET,SOCK_STREAM)

	s.connect((host, port))
	message = input(">>> ")
	
	while message != 'q':
		s.send(message.encode('utf-8'))
		data = s.recv(1024).decode('utf-8')
		# print ("[+] Message sent: " + data)
		message = input(">>> ")
		s.close()

if __name__ == '__main__':
	main()
