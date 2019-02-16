# Use this to print everyone's messages.
import chat_server
import json


def _make_box():
    '''Establishes a read-only connection with the server.'''
    the_connection = chat_server.create_connection_obj()
    the_connection.send('LISTENER')
    return the_connection

def main(reader):
    while True:
        received = reader.receive() # Recieves JSON Data about stuff

        chat_data = json.decode(receive)

        for chat in chat_data:
            if chat["username"]:
                print(chat["username"] + ": ")

            print(chat["message"])
    reader.close()




if __name__ == '__main__':
    main(_make_box())
