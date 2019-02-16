# Handles calls to both chat_input and chat_server
import chat_input
import chat_server



def start_up():
    da_connection = chat_server.create_connection_obj()
    da_connection.messager_connection()

    da_connection.first_message(chat_input.user_name())
    
    return da_connection
    


def main(username:str, da_connection: chat_server.Connection):
    while True:
        message = chat_input.chat()
        if message == 'QUIT':
            break
        da_connection.send(message)

    da_connection.close()




if __name__ == "__main__":

