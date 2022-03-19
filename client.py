import socket

HOST = 'localhost'
PORT = 3333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    outdata = input('please input message:')
    print('send: '+outdata)
    s.send(outdata.encode())

    indata = s.recv(1024)
    if len(indata) == 0:
        s.close()
        print('server closed connection.')
        break
    print('recv: '+indata.decode())

