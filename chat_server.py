import socket


class Connection:
    def __init__(self, sock, in_file, out_file):
        self.in_file = in_file
        self.out_file = out_file
        self.sock = sock

    def send(self, message:str):
        self.out_file.write(message)
        self.out_file.flush()

    def receive(self):
        return self.readline()[:-1]









def create_connection_obj( host:str ='127.0.0.1', port:int = 3000)-> Connection:
    '''Constructs a Connection object.'''
    sock = socket.socket()
    sock.connect( ( host , port ) )
    in_file = socket_puppet.makefile('r')
    out_file = socket_puppet.makefile('w')
    return Connection(sock , in_file , out_file)
