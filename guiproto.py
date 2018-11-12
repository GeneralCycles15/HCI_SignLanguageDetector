# References
# ----------
# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
# https://pythonprogramming.net/tkinter-python-3-tutorial-adding-buttons/?completed=/python-3-tkinter-basics-tutorial/

# Simple enough, just import everything from tkinter.
from tkinter import *

#download and install pillow:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image, ImageTk


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("American Sign Language Interpreter")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
		
        # creating a quit button instance
        quitButton = Button(self, text="Exit",command=self.client_exit)

        # placing the quit button on my window
        quitButton.place(x=650, y=660)
		
		# creating a image button instance
        imgButton = Button(self, text="Image",command=self.showImg)

        # placing the image button on my window
        imgButton.place(x=500, y=660)
    
		# creating a image button instance
        showTextButton = Button(self, text="Show Text",command=self.showText)

        # placing the image button on my window
        showTextButton.place(x=550, y=660)
		
		# creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.open("stock.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=55, y=40)


    def showText(self):
        text = Label(self, text="Insert Result Here")
        text.pack()
        

    def client_exit(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("700x700")

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()
