# Use this to print everyone's messages.
import chat_server


def _make_box():
    '''Establishes a read-only connection with the server.'''
    the_connection = chat_server.create_connection_obj()
    the_connection.send('LISTENER')
    return the_connection

def main(reader):
    while True:
        received = reader.receive()
        if received == '$#AS!@FE':
            break
    reader.close()




if __name__ == '__main__':
    main(_make_box())
