import socket
import os
import os.path
import operator
import sys
import shutil

#def server_program():
host = ''
port=445
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(5)
#conn, address = server_socket.accept()

#print('Coonection from: '+str(address))
print('Waiting for connection from devices . . . ')
#client_req = conn.recv(1024)
#req_str = client_req.decode("utf-8")
while True:
	conn, address = server_socket.accept()
	print('Connection from: '+str(address))
	client_req = conn.recv(1024)
	req_str = client_req.decode("utf-8")
	if req_str == 'downlaod':
		print('This is downloading process requested from connected device. Stanby moode to receive name of the file . . . ')
		client_req = conn.recv(1024)
		file_name = client_req.decode("utf-8")
		file = open(file_name, "rb")
		print('Server is sending a requested file . . .')
		server = file.read(1024)
		while(server):
			conn.send(l)
			server = file.read(1024)
			file.close()
			print('File sent! ')

	elif req_str == 'send':
		print('This is receiving process from connected device . . ')
		client_req = conn.recv(1024)
		file_name = client_req.decode("utf-8")

		file = open(file_name, "wb")
		print('Server is receiving file . . . ')
		server = conn.recv(1024)
		while(server):
			file.write(server)
			server = conn.recv(1024)
		file.close()
		print('File received!')

	elif req_str == 'delete':
		print('This is the process of deleting file from server. . . ')
		client_req = conn.recv(1024)
		file_name = client_req.decode("utf-8")
		if os.path.exists(file_name):
			os.remove(file_name)
			print("The file have been deleted successfully!.")
		else:
			print("The file does not even existed. .")

	conn.close()

