import os

def writeData():
    data = '\nHello World!'
    with open('test.txt', 'a') as f:
        f.write(data)

def openFile():
    with open('test.txt','r') as f:
        data = f.read()
        print(data)

if __name__ == "__main__":
    writeData()
    openFile()
