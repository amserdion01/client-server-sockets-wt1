import socket

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

sock.bind(('localhost', 9015))
sock.listen()
conn, addr = sock.accept()
print(conn, addr)
print(addr, 'connected.')
conn.send(b'You are now connected.\n')
while True:
    data = conn.recv(1024)
    data = data.decode('utf-8')
    if not data: break
    print('Recieved message:', data)
    if data == "hello":
        data = "hi, what's your name?"
        print('Sent message: ', data)
        conn.sendall(bytes(data, encoding='utf8'))
    elif data == 'exit':
        data = "Bye, dear client"
        print('Sent message: ', data)
        conn.sendall(bytes(data, encoding='utf8'))
        break
    elif data == 'Guri':
        data = "Nice to meet you, "+ data
        print('Sent message: ', data)
        conn.sendall(bytes(data, encoding='utf8'))
    elif  data != "I want to connect to the server":
        data = "Try again!"
        print('Sent message: ', data)
        conn.sendall(bytes(data, encoding='utf8'))
conn.close()