
#import tkinter
from tkinter import *

# Be sure to import our other modules
# so we can have access to them
import checkFiles_main
#import checkFiles_func


def load_gui(self):
        
        # Define the form's buttons

        self.btn_browse1 = Button(self.master, text="Browse...", width=12, height=1) #, command=lambda: phonebook_func.addToList(self))
        self.btn_browse1.grid(row=0, column=0, padx=(20,0), pady=(35,0), sticky=W)
        self.btn_browse2 = Button(self.master, text="Browse...", width=12, height=1) #, command=lambda: phonebook_func.onUpdate(self))
        self.btn_browse2.grid(row=1, column=0, padx=(20,0), pady=(10,0), sticky=W)
        self.btn_check   = Button(self.master, text="Check for files...", width=12, height=2) #, command=lambda: phonebook_func.onDelete(self))
        self.btn_check.grid(row=3, column=0, padx=(15,0), pady=(10,10), sticky=E)
        self.btn_close = Button(self.master, text="Close Program", width=12, height=2) #, command=lambda: phonebook_func.ask_quit(self))
        self.btn_close.grid(row=3, column=3, columnspan=1, padx=(15,15), pady=(10,10), sticky=E)

        # Define the form's text boxes
        self.txt_file1 = Entry(self.master,text='')
        self.txt_file1.grid(row=0, column=1, rowspan=1, columnspan=3, padx=(15,15),pady=(35,0),sticky=W+E+N)
        self.txt_file2 = Entry(self.master,text='')
        self.txt_file2.grid(row=1, column=1, rowspan=1, columnspan=3, padx=(15,15),pady=(12,0),sticky=W+E+N)

        #checkFiles_func.create_db(self)
        #checkFiles_func.onRefresh(self)
        



if __name__ == "__main__":
    root = Tk()
    root.grid_columnconfigure(2, weight=12, uniform="foo")
    App = checkFiles_main.ParentWindow(root)
    root.mainloop()
