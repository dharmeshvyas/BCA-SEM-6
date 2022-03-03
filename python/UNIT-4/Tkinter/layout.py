from tkinter import  *

parent  = Tk()
redbutton = Button(parent,text="Red",background="red")
redbutton.pack(side=LEFT)
Greenbutton = Button(parent,text="Green",background="green")
Greenbutton.pack(side=RIGHT)
Bluebutton = Button(parent,text="Blue",background="blue")
Bluebutton.pack(side=TOP)
Yellowbutton = Button(parent,text="Yellow",background="yellow")
Yellowbutton.pack(side=BOTTOM)
parent.mainloop()
