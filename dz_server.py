import socket


ip  = "147.45.158.245"
port = 4444

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((ip,port))
server.listen(5)

client, addr = server.accept()
while True:
    
    messg = client.recv(1024)
    print("Сообщение ",messg.decode("utf-8"))


server.close()