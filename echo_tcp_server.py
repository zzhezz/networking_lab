from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((gethostname(), 1200))

serverSocket.listen(5)
print("The server is ready to accept info")

connectionSocket, address = serverSocket.accept()
print(f"Connection established with {address}")

message = connectionSocket.recv(1024).decode()
print("Got the message from the client: " + message)
if message:
    if "SECRET" in message:
        sum = 0
        res = ""
        for i in message:
            if i.isdigit():
                sum+=1
                res+=i     
        message = "Digits: " + res + "    Count: " + str(sum)                   
        connectionSocket.send(message.encode())
    else:
        message = "Secret code not found."
        connectionSocket.send(message.encode())    

connectionSocket.close()
