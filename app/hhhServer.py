from socket import *
import sys
import os
import time

class MyHttpServer:
	def __init__(self):
		# Set the port of the server
		self.port = int(os.getenv('VCAP_APP_PORT', '8090'))
		# Set thte IP address of the server
		self.IP_Address = str(os.getenv('VCAP_APP_HOST', 'localhost'))
	
	# Function to set the socket of the server
	def pySocket(self):
		# Create a new socket 
		self.MyServer = socket(AF_INET,SOCK_STREAM)
		# Bind the IP address and the port number to the socket 
		self.MyServer.bind((self.IP_Address,self.port))
		# Listening
		self.MyServer.listen(1)
		self.getRequest()
	
	# Function to pack the head 
	def header_packer(self,statu_code,content_type,Content_Len):
		# Initialize head as string
		head = ''
		# If the statu_code is 200
		if(statu_code == 200):
			# Make the head "HTTP OK"
			head = 'HTTP/1.1 200 OK \r\n'
		# If the statu_code is 404
		elif(statu_code == 404):
			# Make the head "HTTP 404 Not Found"
			head = 'HTTP/1.1 404 Not Found\n'
		# Get the current time 
		current_time = time.strftime('%a,%d %b %y %H:%M',time.localtime())
		# Beijing time 
		current_time += ' BJS'
		# Get current time 
		head += 'Date: '+current_time+'\n'
		# Pack the file's content_type
		head += 'Content-Type: '+content_type+'\n'
		# Pack hte content_length
		head += 'Content-Length: '+str(Content_Len)+'\n'
		# Pack the sever name 
		head += 'Server: MyHttpServer \n'
		# End 
		head += '\n'
		return head
		
	# Function to get the request from the website
	def getRequest(self):
		while True:
			try:
				# Set up a new connection from the client
				connectionSocket, address = self.MyServer.accept()
				# Get the request from the website
				request = connectionSocket.recv(1024).decode()
				# To handle the requist of the website
				self.handleRequest(request,connectionSocket)
			except KeyboardInterrupt:
				break
	
    # Handle the message from website	
	def handleRequest(self,request,connectionSocket):
		self.connectionSocket = connectionSocket
		fp = open('Capture.html','rb')
		response_file = fp.read()
		Content_Len = len(response_file)
		fp.close()
		# The packet header is 200
		response_head = self.header_packer(200,'text/html',Content_Len)
		response = response_head.encode()
		response += response_file

		self.connectionSocket.send(response)
		# Close the socket 	
		self.connectionSocket.close()

# Start the function
if __name__ == '__main__':			
	server = MyHttpServer()
	server.pySocket()

