####   implement gui, use scroll and others from tkinter
####   combine chat and chatbox into one file.

import chat_server
import tkinter as tk
import time

class gui:

    def __init__(self, da_connection):
        self.connection = da_connection
        
        self.mainbox = tk.Tk()
        self.mainbox.geometry("500x500")
        self.mainbox.title("Abrupt Cow Chat")

        # text viewing window
        self.viewer = tk.Text(self.mainbox, height=2, width=30)
        self.viewer.place( x=10 , y=10 , width=430 , height=400 )

        #  scrollbar object
        self.scroller = tk.Scrollbar( self.mainbox )
        self.scroller.place( x=455 , y=10 , width=25 , height=400 )


        # entry box to input messages.
        self.message_box = tk.Entry()
        self.message_box.place( x=10 , y=430 , width=360 , height=30 )
        
        # button for sending messages
        self.sender = tk.Button( self.mainbox , text="Send Message" )
        self.sender.place( x=380 , y=430 , width=100 )
        
        
        # syncs the scrollbar with the text window.
        self.scroller.config( command=self.viewer.yview )
        self.viewer.config( yscrollcommand=self.scroller.set )

        

        # binds keyboard shortcuts to send messsage.
        self.mainbox.bind('<Return>' , self.get_message_to_send)
        self.sender.bind('<Button-1>' , self.get_message_to_send)
        self.queue = ''
        
        self.message = ''
        
        while True:
            self.mainbox.update()
            self.u()
     


    def get_message_to_send(self,event):

        s = self.message_box.get()
        if s != '':
            self.message_box.delete(0, tk.END)
            
            self.connection.send(s)
                
            return



    def u(self):
        k = self.connection.receive()
        if k != 'E O F: EOF':
            
            k = k.encode(encoding='utf-8')
            self.viewer.delete('1.0', tk.END)
            
            self.viewer.insert(tk.END , k)
            self.viewer.insert(tk.END , '\n')
            self.viewer.yview_moveto( 1 )


