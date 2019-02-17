import socket
import json

HOST = 'abruptcow.tech'
PORT = 4000


class Connection:
    def __init__( self , sock ):
        self.sock = sock
        self.out_file = self.sock.makefile('w')
        self.in_file = self.sock.makefile('r')


    def send(self, message:str):
        self.out_file.write(message)
        self.out_file.flush()


    def receive(self):
        try:
            received = self.in_file.readline()[:-1]     # Recieves JSON Data about stuff
        
        except UnicodeDecodeError:
            return '<Emoji>'

        if received != 'E O F: EOF':    
            chat_data = json.loads(received)
               
            l = []
            for chat in chat_data:
                l.append(chat["username"] + ": " + chat["message"]) 
            return '\n'.join(l)
        return received
    
    
    def first_message(self, username):
        self.send('USER ' + username)
        return self.in_file.readline()

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




