import rsa
from os import listdir
from os.path import isfile, join

import os,shutil

mypath = "C://Users/Dhana/Desktop/Conf Docs/Locker/Sender/"
otherpath = "C://Users/Dhana/PycharmProjects/dsgsec2/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


privkey = rsa.PrivateKey.load_pkcs1(file_open(otherpath+'privatekey.key'))


def digisignature(mypath,filename,privkey):
    message = file_open(mypath+filename)
    #hash_value = rsa.compute_hash(message, 'SHA-512')  # optional

    signature = rsa.sign(message, privkey, 'SHA-512')
    #now = datetime.datetime.now()
    #time = "\n" + now.strftime("%d-%m-%Y %H:%M")

    s = open(mypath+"To Send/"+filename+".txt",'wb')
    s.write(signature)
    #s.write(time.encode())
    s.close()

def CopyFiles(mypath,filename,movepath):
    shutil.copy(mypath+filename,movepath)

for i in onlyfiles:
    if(i!='0. DSG.bat'):
        #print(i)
        digisignature(mypath,i,privkey)

for i in onlyfiles:
    if (i != '0. DSG.bat'):
        CopyFiles(mypath,i,mypath+"To Send/")
