import socket, select, sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = str(sys.argv[1])
port = int(sys.argv[2])
server.connect((ip, port))

while True:
    sockets_list = [sys.stdin, server]
    read_sockets, write_socket, serror_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message= socks.recv(2048)
            print message
        else:
            alias = "<astor>"
            message = alias + sys.stdin.readline()
            server.send(message)
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
