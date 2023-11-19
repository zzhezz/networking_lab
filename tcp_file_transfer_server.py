from socket import *

# The IP address of the server


# Create a socket object
server_socket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the IP and port
server_socket.bind((gethostname(), 5000))
# Listen for incoming connections
server_socket.listen(5)
print(f'Server listening')

# Accept a connection
connection, address = server_socket.accept()
print(f'Connected by {address}')

# Open the file to write the incoming data
with open('received_file.txt', 'wb') as f:
    while True:
        data = connection.recv(1024)
        if not data:
            break
        f.write(data)

# Close the connection
connection.close()
print('File received and connection closed.')
