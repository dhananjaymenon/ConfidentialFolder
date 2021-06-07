#This stands for Alert Message 2. (used incase invalid decryption password is given)

import cv2
import random
import os
import smtplib
from email.message import EmailMessage
import imghdr


cam = cv2.VideoCapture(0)
n = random.randint(1000, 9999)
ret, img = cam.read()
cv2.imshow("Test",img)

k=cv2.waitKey(1000)

file='C://dsg//img//'+str(n)+'.jpg'
cv2.imwrite(file,img)
cam.release()
cv2.destroyAllWindows()


#SEND EMAIL
#INSERT YOU DETAILS HERE
email = ""
password = ""
enduser = ""
#########################

msg = EmailMessage()
msg['Subject'] = 'SECURITY ALERT'
msg['From'] = email
msg['To'] = enduser
msg.set_content('Your first Passcode is compromised. Change it if this is not you.'\
                'There was an attempt to decrypt files in your system. This was reported due to an incorrect password entered.' \
           'If this was you, Ignore the message')

with open('C://dsg//img//'+str(n)+'.jpg','rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

    smtp.login(email,password)
    smtp.send_message(msg)

