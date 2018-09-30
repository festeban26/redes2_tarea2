import socket, ssl
import os

def do_something(data):
    print('Server Response: ' + data)
    return False

def pingable(hostname):
    response = os.system("ping -c 1 " + hostname) #and then check the response
    if response == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Require a certificate from the server. We used a self-signed certificate
    # so here ca_certs must be the server certificate itself.
    ssl_sock = ssl.wrap_socket(s,
                               ca_certs="./server.crt",
                               cert_reqs=ssl.CERT_REQUIRED)

    ssl_sock.connect(('localhost', 10024))

    errorpath = './'
    errorfile = 'sserver.log'
    errorpath = os.path.join(errorpath, errorfile)

    file = open('./dr_hosts.txt','r')
    file_txt = file.read()

    file_vals = file_txt.split('\n')

    file.close()

    if file_vals is not None:

        data = ''
        for val in file_vals:
            result = pingable(val)
            data = data + val + " - " + str(result) + "\n"

        ssl_sock.write(data.encode("ASCII"))

        #data = ssl_sock.read()
        #while data:
        #    if not do_something(data):
        #        break
        #    data = ssl_sock.read()

    ssl_sock.close()
