# Use this to print everyone's messages.
import chat_server


def _make_box():
    '''Establishes a read-only connection with the server.'''
    reader = chat_server.create_connection_obj()
    reader.viewer_connection()
    return reader

def main(reader):
    while True:
        print(reader.receive())



if __name__ == '__main__':
    main(_make_box())

