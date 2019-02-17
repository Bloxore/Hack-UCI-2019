# Handles calls to both chat_input and chat_server
import chat_server
import chat_gui
import chat_input



def start_up(username):
    da_connection = chat_server.create_connection_obj()

    da_connection.first_message(username)

    return da_connection



def main(username:str, da_connection: chat_server.Connection):
    
    try:
        the_box = chat_gui.gui(da_connection)
    except:
        pass

    da_connection.close()


                                                                                
                                                                                

if __name__ == "__main__":
    name = chat_input.user_name()
    thing = start_up(name)
    main(name, thing)
