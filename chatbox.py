# Use this to print everyone's messages.
import chat_server
import json


def _make_box():
    '''Establishes a read-only connection with the server.'''
    the_connection = chat_server.create_connection_obj()
    the_connection.send('LISTENER')
    return the_connection

def receive(reader):
    received = reader.receive() # Recieves JSON Data about stuff

    chat_data = json.loads(received)
    
    reader.close()

    for chat in chat_data:
        return chat["username"] + ": " + chat["message"]





if __name__ == '__main__':
    main(_make_box())
