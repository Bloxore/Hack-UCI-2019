# Handles calls to both chat_input and chat_server
import chat_server
import chat_gui
import chat_input



def start_up(username):
    da_connection = chat_server.create_connection_obj()

    print(da_connection.first_message(username))

    return da_connection



def main(username:str, da_connection: chat_server.Connection):
    
    the_box = chat_gui.gui(da_connection)

    da_connection.close()
    print('i closed the connection!')


                                                                                
                                                                                

if __name__ == "__main__":
    name = input('Enter username: ')
    thing = start_up(name)
    main(name, thing)
