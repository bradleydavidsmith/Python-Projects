# Python Ver:   3.8.1
#
# Purpose:      Check Files/Tkinter Demo. demonstration OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested to work with Windows 10.


from tkinter import *

# Be sure to import the other modules
import checkFiles_gui
#import checkFiles_func

# Frame is the Tkinter fram class that our own class will inherit from
class ParentWindow(Frame):
        def __init__ (self, master, *args, **kwargs):
            Frame.__init__ (self, master, *args, **kwargs)

            root.grid_columnconfigure(2, weight=12, uniform="foo")

            ## Define our master frame configuration
            ###self.master = master
            self.master.minsize(500,170) #(Height, Width)
            self.master.maxsize(500,170)
            # This CenterWindow method will center our app on the user's screen
            #checkFiles_func.center_window(self,500,300)
            self.master.title('Check Files')
            self.master.config(bg='#F0F0F0')
            
            # This protocol method is a tkinter built-in method to catch if
            # the user clicks the upper corner, "X" on Window OS.
            #self.master.protocol('WM_DELETE_WINDOW', lambda: checkFiles_func.ask_quit(self))

            # load in the GUI widgets from a seperate module,
            # keeping your code comparmentalized and clutter free
            checkFiles_gui.load_gui(self)


if __name__ == "__main__":
    root = Tk()
    #root.grid_columnconfigure(2, weight=12, uniform="foo")
    App = ParentWindow(root)
    root.mainloop()
