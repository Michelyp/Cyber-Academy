import socket
size = 512
host = 'localhost'
port = 5000
#family = Internet, type = stream socket means TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((host,port))
sock.listen(5)
print('listening in port '+str(port))
c,addr= sock.accept()
data = c.recv(size)
if data ==512:
    print("connection from: ", port)
sock.close()
