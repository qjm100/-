import socket

HOST = ''
POST = int(input ('对方端口'))
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((HOST, POST))
# 实现通信循环
data = True
while data:
    data, addr = sock.recvfrom(1024)#缓冲区大小
    if data == b'q':
        break
    print("Receive a message from " ,data.decode('utf-8'))
    sock.sendto (data,addr)

sock.close()
