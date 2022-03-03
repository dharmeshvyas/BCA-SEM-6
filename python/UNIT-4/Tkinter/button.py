import tkinter
windows = tkinter.Tk()
windows.title("Button")

button_widget =  tkinter.Button(windows,text="click here")
button_widget.pack()
windows.mainloop()