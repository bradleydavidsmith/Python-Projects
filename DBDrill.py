import sqlite3
import os

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_textfiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
    conn.commit()


    for file in fileList:
        # Split the extension from the path and normalize it to lowercase:
        ext = os.path.splitext(file)[1].lower()

        # If it's a text file, ...
        if ext == '.txt':
            
            # Add the file to the database table.
            cur.execute("INSERT INTO tbl_textfiles(col_filename) VALUES (?)", \
                        (file,))


    # Print out all the filename in the database table
    cur.execute("SELECT col_filename from tbl_textfiles")
    varFiles = cur.fetchall()
    print("These are the files in the database:")
    for file in varFiles:
        print(file[0])
        

    
