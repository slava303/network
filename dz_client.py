import socket
import random

ip = input("Введите IP адрес: ")
port = 4444
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((ip,port))


while True:
    mess = input()
    client.send(mess.encode())

client.close()