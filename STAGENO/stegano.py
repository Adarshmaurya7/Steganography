# Project based on stegnography ( hiding text inside image )
import cv2  
import os  # for read and write process
import string   # for ASCII to Binary conversion


img = cv2.imread("Image.jpeg") # Fetching image for stegeno process

msg = input("Enter your secret message you want to insert:")
password = input("Enter a passcode :")

d = {}  # creation of two dictionary for storing ASCII value and Pixel value
c = {}

#ENCRYPTION-----------------------------------------------------------------------


for i in range(255):   #iterate over ASCII value and comparing it
     d[chr(i)] = i
     c[i] = chr(i)

m = 0  # use it for RGB color
n = 0
z = 0


for i in range(len(msg)):    # mix the message and ASCII value
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3


cv2.imwrite("steganoImage.jpg", img)
os.system("start steganoImage.jpg") # Use 'start' to open the image on Windows


message = ""
n = 0
m = 0
z = 0

#DECRYPTION ---------------------------------------------------------------------------

pas = input("Enter passcode for Decryption of message :")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
     print("YOU ARE NOT AUTHORIZED")
