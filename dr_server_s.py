import socket, ssl
import threading


def do_something(data, addr):
    print("do_something: "+ data.decode('ASCII'))
    file = open('./server_side_ssl_' + str(addr[0]) + "_" + str(addr[1]) + '.txt', 'w+')
    file.write(data.decode('ASCII'))
    file.close()
    return False

def deal_with_client(connstream, fromaddr):
    data = connstream.read()

    while data:
        if not do_something(data, fromaddr):
            break
        data = connstream.read()

    #connstream.write('OK.')
    #connstream.shutdown(socket.SHUT_RDWR)
    connstream.close()

if __name__ == '__main__':

    bindsocket = socket.socket()
    bindsocket.bind(('', 10024))
    bindsocket.listen(5)

    while True:
        newsocket, fromaddr = bindsocket.accept()
        connstream = ssl.wrap_socket(newsocket,
                                 server_side=True,
                                 certfile="./server.crt",
                                 keyfile="./server.key")
        try:
            threading.Thread(target=deal_with_client, args=(connstream,fromaddr)).start()
        finally:
            print('Done with thread')