from socket import *

host_name = "10.18.128.218"
port_number = 1200

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((host_name, port_number))

message = input("enter something: ")
clientSocket.send(message.encode()) #把string变为bit

upperMessage = clientSocket.recv(1024).decode() #把bit变为string
print("the messgae from the server: " + upperMessage)

clientSocket.close()

