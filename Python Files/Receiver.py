import rsa
from os import listdir
from os.path import isfile, join
import shutil

mypath = "C://Users/Dhana/Desktop/Conf Docs/Locker/Receiver/"
otherpath = "C://Users/Dhana/PycharmProjects/dsgsec2/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


pubkey = rsa.PublicKey.load_pkcs1(file_open(otherpath+'publickey.key'))

def verifier(mypath,file,pubkey):
    message = file_open(mypath+file)
    # message2 = message.decode()
    # message2 = message2[:-16]
    # message = message2.encode()
    #print(type(message))
    signature = file_open(mypath+"signatures/"+file+".txt")

    try:
        rsa.verify(message,signature,pubkey)
        print("Signature successfully verified")
        s = open(mypath+"verification/V-"+file+".txt", 'w')
        s.write("Signature successfully verified")
        s.close()

    except:
        print("Error - Signature could not be verified")
        s = open(mypath +"verification/E-"+ file + ".txt", 'w')
        s.write("Error - Signature could not be verified")
        s.close()

def MoveFiles(mypath,filename,movepath):
    shutil.move(mypath + filename, movepath)


#Move only signatures
for i in onlyfiles:
    if(i[-4:] == '.txt'):
        #print(i)
        MoveFiles(mypath,i,mypath+"signatures/")

onlyfiles2 = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in onlyfiles2:
    if(i!='0. DSG.bat'):
        #print(i)
        verifier(mypath,i,pubkey)
