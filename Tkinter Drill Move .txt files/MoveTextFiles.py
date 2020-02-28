# Python Ver:   3.8.1
#
# Purpose:      Move Text Files/Tkinter Demo. demonstration OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested to work with Windows 10.
#
# Future Improvements:
#               1) Since the user can edit the folder name, add a check to verify that the folder actually exists.
#               2) Warn the user if no text files are found in the source folder.
#               3) Since SQLite has no date column type, find the best way to represent a date.



from tkinter import *
from tkinter import filedialog
import datetime as dt
import os, shutil, sqlite3


def load_gui(self):
        
        # Define the form's buttons

        self.btn_browse1 = Button(self.master, text="Source Folder...", width=12, height=1, command=lambda: setFolder(self, self.txt_folder1, "source"))
        self.btn_browse1.grid(row=0, column=0, padx=(20,0), pady=(35,0), sticky=W)
        self.btn_browse2 = Button(self.master, text="Target Folder...", width=12, height=1, command=lambda: setFolder(self, self.txt_folder2, "destination"))
        self.btn_browse2.grid(row=1, column=0, padx=(20,0), pady=(10,0), sticky=W)
        self.btn_check   = Button(self.master, text="Move *.txt files...", width=12, height=2, command=lambda: copyTextFiles(self))
        self.btn_check.grid(row=3, column=0, padx=(15,0), pady=(10,10), sticky=E)
        self.btn_close = Button(self.master, text="Close Program", width=12, height=2, command=lambda: os._exit(0))
        self.btn_close.grid(row=3, column=3, columnspan=1, padx=(15,15), pady=(10,10), sticky=E)

        # Define the form's text boxes
        self.txt_folder1 = Entry(self.master,text='')
        self.txt_folder1.grid(row=0, column=1, rowspan=1, columnspan=3, padx=(15,15),pady=(35,0),sticky=W+E+N)
        self.txt_folder2 = Entry(self.master,text='')
        self.txt_folder2.grid(row=1, column=1, rowspan=1, columnspan=3, padx=(15,15),pady=(12,0),sticky=W+E+N)

def setFolder(self, text_folder, var_folderType):
        # Bring up a dialog box to ask the user for the folder path
        folder = filedialog.askdirectory(parent=self, initialdir='"'+os.getcwd()+'"', title="Please select the " + var_folderType + " folder:")

        # Put the folder path into the text_file Entry field
        text_folder.delete(0,END)
        text_folder.insert(0,folder)

def copyTextFiles(self):
        sourceFolder = self.txt_folder1.get()
        targetFolder = self.txt_folder2.get()

        # Go through all the files in the folder, selecting only the .txt files.
        for filename in os.listdir(sourceFolder):
            if filename.endswith(".txt"):
                sourceFile   = os.path.join(sourceFolder, filename)
                
                # Get the modify time
                mtime = os.path.getmtime(sourceFile)
                
                # Convert the modify date of the file to a string that SQL Lite can sort, since SQL doesn't have a date type
                modifyDateString = dt.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d_%H:%M:%S')
                print(sourceFile, modifyDateString)

                # Move the text file
                shutil.move(sourceFile, targetFolder)
                targetFile = os.path.join(targetFolder, filename)

                # Write the file and modify date to the database.
                with sqlite3.connect('copyTxtFile.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO tbl_copiedTxtFile(col_txt_file, col_mod_date) VALUES (?,?)", (targetFile, modifyDateString))

def create_db():
    with sqlite3.connect('copyTxtFile.db') as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_copiedTxtFile( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txt_file TEXT, \
        col_mod_date TEXT \
        );")
    # You must commit to save changes & close the database connection
        conn.commit()
    # The with statement auto-closes the connection, conn.
    

# Frame is the Tkinter fram class that our own class will inherit from
class ParentWindow(Frame):
        def __init__ (self, master, *args, **kwargs):
            Frame.__init__ (self, master, *args, **kwargs)

            ## Size the master window
            self.master.minsize(500,170) #(Height, Width)
            self.master.maxsize(500,170)

            # Name the window, and give it a color.
            self.master.title('Copy Text Files')
            self.master.config(bg='#F0F0F0')
            

            # Load in the GUI widgets using a seperate function.
            load_gui(self)


if __name__ == "__main__":
    create_db()
    root = Tk()
    root.grid_columnconfigure(2, weight=12, uniform="foo")
    App = ParentWindow(root)
    root.mainloop()
