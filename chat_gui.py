####   implement gui, use scroll and others from tkinter
####   combine chat and chatbox into one file.

import tkinter as tk

mainbox = tk.Tk()
mainbox.geometry("500x500")


# text viewing window
viewer = tk.Text(mainbox, height=2, width=30)
viewer.place( x=10 , y=10 , width=360 , height=360 )

#  scrollbar object
scroller = tk.Scrollbar( mainbox )
scroller.place( x=390 , y=10 , width=25 , height=360 )

# syncs the scrollbar with the text window.
scroller.config( command=viewer.yview )
viewer.config( yscrollcommand=scroller.set )


def get_message(event):
    s = ENTRY.get()
    if s != '':
        ENTRY.delete(0, tk.END)
        update(s)
        return s

def update(message:str):
        viewer.insert(tk.END , message)
        viewer.insert(tk.END , '\n')
        viewer.yview_moveto( 1 )


ENTRY = tk.Entry()
ENTRY.place(x=10, y=400, width=360, height=30)


button = tk.Button(mainbox, text="Send Message")
button.place(x=380,y=400,width=100)




mainbox.bind('<Return>', get_message)
button.bind('<Button-1>', get_message)


mainbox.mainloop()
