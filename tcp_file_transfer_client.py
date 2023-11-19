from socket import *

# The IP address of the server
server_ip = '10.18.128.218'
server_port = 5000

# Create a socket object
client_socket = socket(AF_INET, SOCK_STREAM)

# Connect the client to the server
client_socket.connect((server_ip, server_port))

# The path to the file you want to send
file_path = 'sampleText.txt'

# Open the file to read in binary mode
with open(file_path, 'rb') as f:
    # Read the file in chunks
    while True:
        bytes_read = f.read(1024)
        if not bytes_read:
            break
        client_socket.sendall(bytes_read)

# Close the socket
client_socket.close()
print('File sent.')
