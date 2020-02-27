# Python Ver:   3.8.1
#
# Purpose:      Check Files/Tkinter Demo. demonstration OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships and the
#               askdirectory() method
#
# Tested OS:    This code was written and tested to work with Windows 10.


from tkinter import *
from tkinter import filedialog
import os

def load_gui(self):
        
        # Define the form's button

        self.btn_browse1 = Button(self.master, text="Browse...", width=12, height=1, command=lambda: setFolder(self))
        self.btn_browse1.grid(row=0, column=0, padx=(20,0), pady=(35,0), sticky=W)

        # Define the form's text boxes
        self.txt_folder = Entry(self.master,text='')
        self.txt_folder.grid(row=0, column=1, rowspan=1, columnspan=3, padx=(15,15),pady=(35,0),sticky=W+E+N)        

def setFolder(self):
        # Bring up a dialog box to ask the user for the folder path
        folder = filedialog.askdirectory(parent=self, initialdir='"'+os.getcwd()+'"', title="Please select a folder:")

        # Put the folder path into the text_file Entry field
        self.txt_folder.delete(0,END)
        self.txt_folder.insert(0,folder)

# Frame is the Tkinter fram class that our own class will inherit from
class ParentWindow(Frame):
        def __init__ (self, master, *args, **kwargs):
            Frame.__init__ (self, master, *args, **kwargs)

            ## Define our master frame configuration
            self.master.minsize(500,100) #(Width, Height)
            self.master.maxsize(500,100)
            
            # Set the window's title and color
            #checkFiles_func.center_window(self,500,300)
            self.master.title('Choose A Folder')
            self.master.config(bg='#F0F0F0')

            # load in the GUI widgets
            load_gui(self)


if __name__ == "__main__":
    root = Tk()
    root.grid_columnconfigure(2, weight=12, uniform="foo")
    App = ParentWindow(root)
    root.mainloop()
