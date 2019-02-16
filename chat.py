# Handles calls to both chat_input and chat_server
import chat_input
import chat_server



def start_up():
    da_connection = chat_server.create_connection_obj()
    name = chat_input.user_name()
    da_connection.first_message(name)
    return da_connection
    


def main(username:str, da_connection: chat_server.Connection):
    while True:
        pass



if __name__ == "__main__":

