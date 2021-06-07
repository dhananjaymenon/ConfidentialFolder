from os import listdir
import os,shutil
from os.path import isfile, join

mypath = "C://Users/Dhana/Desktop/Encrypt Folder/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
movepath = "C://Users/Dhana/Desktop/Encrypt Folder/Encrypted"

def Encrypt(mypath,filename, key):
    file = open(mypath+filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(filename, "wb")
    file.write(data)
    file.close()

def MoveFiles(mypath,filename,movepath):
    shutil.move(mypath+filename,movepath)


for i in onlyfiles:
    if(i!='Encrypter.bat'):
        #print(i)
        Encrypt(mypath,i,5)

onlyfiles2 = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in onlyfiles2:
    if(i!='Encrypter.bat'):
        #print(i)
        MoveFiles(mypath,i,movepath)


