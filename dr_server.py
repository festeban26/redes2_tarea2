import socket
import threading

def do_something(data):
    print("do_something: "+ data)
    return False

def deal_with_client(conn, addr):
    data = ''
    file = open('./server_side_'+str(addr[0])+"_"+str(addr[1])+'.txt', 'w+')
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                file.write(data.decode('ASCII'))
    file.write("\n")
    file.close()

if __name__ == '__main__':

    bindsocket = socket.socket()
    bindsocket.bind(('', 10023))
    bindsocket.listen(5)

    while True:
        newsocket, fromaddr = bindsocket.accept()

        try:
            threading.Thread(target=deal_with_client, args=(newsocket, fromaddr)).start()
        finally:
            print('Done with thread')