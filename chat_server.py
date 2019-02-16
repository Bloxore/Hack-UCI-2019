import socket
import json

HOST = '35.235.78.32'
PORT = 4000


class Connection:
    def __init__( self , sock ):
        self.sock = sock
        self.out_file = self.sock.makefile('w')
        self.in_file = self.sock.makefile('r')


    def send(self, message:str):
        self.out_file.write(message)
        self.out_file.flush()

    def _receive(self):
        received = self.in_file.readline()[:-1]
        print(received)
        return received

    def receive(self):
        received = self.sock._receive() # Recieves JSON Data about stuff

        chat_data = json.loads(received)

        reader.close()

        return '\n'.join([chat["username"] + ": " + chat["message"] for chat in chat_data])

    
    
    def first_message(self, username):
        self.send('USER ' + username)
        return self.receive()

    def close(self):
        if self.in_file != None:
            self.in_file.close()
        if self.out_file != None:
            self.out_file.close()





def create_connection_obj()-> Connection:
    '''Constructs a Connection object.'''
    sock = socket.socket()
    sock.connect( ( HOST , PORT ) )
    return Connection( sock )
