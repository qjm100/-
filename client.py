import socket

HOST = input ('ip:')
PORT = int (input ('端口:'))
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = '你好'
# 实现通信循环
while data:
    sock.sendto (data.encode('utf-8'),(HOST,PORT))
    if data == 'q':
        break
    elif data == None:
        print('不合法字符None')
        break
    data,addr = sock.recvfrom (1024)
    print ('收到服务端返回值\n',data.decode('utf-8'))
    data = input ('send:')


sock.close()
