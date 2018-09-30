import socket
import os

def do_something(data):
    print('Server Response: ' + data)
    return False

def pingable(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('localhost', 10023))

    errorpath = './'
    errorfile = 'error_speedtest.log'
    errorpath = os.path.join(errorpath, errorfile)

    file = open('./dr_hosts.txt','r')
    file_txt = file.read()

    file_vals = file_txt.split('\n')

    file.close()

    if file_vals is not None:

        data = ''
        for val in file_vals:
            result = pingable(val)
            data = data + val + ' - ' + str(result) + '\n'

        print(data)

        s.sendall(data.encode('ASCII'))

    s.close()
