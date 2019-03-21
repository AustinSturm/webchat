import socket, select, sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = str(sys.argv[1])
port = int(sys.argv[2])
server.connect((ip, port))


def history(socket, hist):
    socket.send("<chotbot> History:")
    for message in hist[len(hist)-5:]:
        socket.send(message)
    return 1


while True:
    sockets_list = [sys.stdin, server]
    read_sockets, write_socket, serror_socket = select.select(sockets_list, [], [])

    hist = []
    for socks in read_sockets:
        if socks == server:
            message= socks.recv(2048)
            print message
            if message.find(":") > 0:
                if message.find("allah") > -1:
                    message = "<chatbot> allah akhbar....Boom....BOOM...CRASH"
                    server.send(message)
                    sys.stdout.write(message)
                    sys.stdout.flush()

                hist.append(message)
                if message.find("history") > -1:
                    history(server, hist)


        else:
            alias = "<chatbot>"
            message = alias + sys.stdin.readline()
            server.send(message)
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
