import socket

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

sock.connect(('localhost', 9015))
sock.sendall(b'I want to connect to the server')
while True:
    data = sock.recv(1024)
    data = data.decode('utf-8')
    print('Received:', data)
    if data == "Bye, dear client":
        break
    send = input()
    sock.sendall(bytes(send, encoding='utf8'))
    
sock.close()