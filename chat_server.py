import socket


class Connection:
    def __init__(self, sock, in_file, out_file):
        self.in_file = in_file
        self.out_file = out_file
        self.sock = sock



def _get_connect():
    sock_puppet = socket.socket()
    sock_puppet.connect(('127.0.0.1',3000))
    in_file = socket_puppet.makefile('r')
    out_file = socket_puppet.makefile('w')
