
import os

fName = 'Hello.txt'

fPath = os.getcwd()

abPath = os.path.join(fPath, fName)

print(abPath)
