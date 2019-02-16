####   implement gui, use scroll and others from tkinter
####   combine chat and chatbox into one file.

import tkinter as tk

class gui():

    def __init__(self):
        
        self.mainbox = tk.Tk()
        self.mainbox.geometry("500x500")


        # text viewing window
        self.viewer = tk.Text(self.mainbox, height=2, width=30)
        self.viewer.place( x=10 , y=10 , width=360 , height=360 )

        #  scrollbar object
        self.scroller = tk.Scrollbar( self.mainbox )
        self.scroller.place( x=390 , y=10 , width=25 , height=360 )


        # entry box to input messages.
        self.message_box = tk.Entry()
        self.message_box.place( x=10 , y=400 , width=360 , height=30 )
        
        # button for sending messages
        self.button = tk.Button( self.mainbox , text="Send Message" )
        self.button.place( x=380 , y=400 , width=100 )
        

        # syncs the scrollbar with the text window.
        self.scroller.config( command=self.viewer.yview )
        self.viewer.config( yscrollcommand=self.scroller.set )

        # binds keyboard shortcuts to send messsage.
        self.mainbox.bind('<Return>' , self.get_message_to_send)
        self.button.bind('<Button-1>' , self.get_message_to_send)

        self.mainbox.mainloop()
     
    
    def get_message_to_send(self,event):
        s = self.message_box.get()
        if s != '':
            self.message_box.delete(0, tk.END)
            return s

    def update(self, message:str):
            self.viewer.insert(tk.END , message)
            self.viewer.insert(tk.END , '\n')
            self.viewer.yview_moveto( 1 )



   
    




