import socket


class Connection:
    def __init__( self , sock )
        self.sock = sock
        self.in_file = None
        self.out_file = None

    def viewer_connection( self ):
        self.in_file = self.sock.makefile('r')
            

    def messager_connection( self ):
        self.viewer_connection()
        self.out_file = self.sock.makefile('w')

    def send(self, message:str):
        self.out_file.write(message)
        self.out_file.flush()

    def receive(self):
        return self.readline()[:-1]

    def first_message(username:str):
        self.send('HELLO, I AM ' + username)

    def close(self):
        if self.in_file != None:
            self.in_file.close()
        if self.out_file != None:
            self.out_file.close()
        




def create_connection_obj( host:str ='127.0.0.1', port:int = 3000)-> Connection:
    '''Constructs a Connection object.'''
    sock = socket.socket()
    sock.connect( ( host , port ) )
    return Connection( sock )
