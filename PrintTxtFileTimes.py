
import os

def printTxtFileTimes():
    ## Get the current folder path
    fPath = os.getcwd()

    ## Create a path to the folder we're interested in
    fFolder = os.path.join(fPath,'A')

    ## Go through eachof these files:
    for file in os.listdir(fFolder):

        # Split the extension from the path and normalize it to lowercase:
        ext = os.path.splitext(file)[1].lower()

        # If it's a text file, ...
        if ext == '.txt':

            # get the text file's modify time, and ...
            txtFile = os.path.join(fFolder, file)
            mtime = os.path.getmtime(txtFile)

            # print the filename and modify time (mtime).
            print(txtFile + ' ' + str(mtime))


if __name__ == "__main__":
    printTxtFileTimes()
