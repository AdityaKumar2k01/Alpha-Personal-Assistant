# # # # import pyautogui, time
# # # # time.sleep(5)
# # # # while True:
# # # #     #pyautogui.typewrite("Hello Safiqul ,Hello Anupam ,Hello Keshav ")
# # # #     #pyautogui.typewrite("Hello Safiqul ,Hello Anupam ,Hello Keshav ")
# # # #     pyautogui.typewrite("Hello Anupam !!!")
# # # #     pyautogui.press("enter")
    
# # # #impress your crush using python

# # # # importing the turtle module
# # # import turtle

# # # # Creating an wr object of turtle
# # # wr = turtle.Turtle()

# # # # Setting Color
# # # wr.fillcolor('red')
# # # # Filling the color
# # # wr.begin_fill()

# # # # Start Drawing the Heart
# # # wr.left(140)
# # # wr.forward(113)

# # # # Drawing the carve of heart
# # # for i in range(200):
# # #     wr.right(1)
# # #     wr.forward(1)
# # # wr.left(120)


# # # # Drawing the carve of heart
# # # for i in range(200):
# # #     wr.right(1)
# # #     wr.forward(1)

# # # wr.forward(112)
# # # # Ending the filling color
# # # wr.end_fill()
# # # wr.ht()/


# # # Importing the required module
# # # Find more projects at codewithcurious.com
# # import pywhatkit as kit
# # import cv2

# # # Converting text into handwritting image
# # kit.text_to_handwriting("Hey theere! curious programmer here.", save_to="writing.png")

# # # Saving the Generated Image
# # img = cv2.imread("writing.png")

# # # Showing the Generated image
# # cv2.imshow("Text to Handwriting", img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # import all the required packages
# # Visit : codewithcurious.com for more projects
# from tkinter import *
# import random
# import pyperclip

# # To create a root window of GUI in python
# tk=Tk()
# tk.geometry('300x300')
# tk.configure(background='yellow')

# # To store/retrieve the string value entered by user
# pswd=StringVar()

# # To store/retrieve the Integer value entered by user
# passlen=IntVar()
# passlen.set('Enter Length')

# # Function to generate a random password
# def password_generator():
#     characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*()'
#     password=''
#     if passlen.get()>=8:
#         for i in range(passlen.get()):
#             password+=random.choice(characters)
#         pswd.set(password)

# # Function to copy generated password to clipboard
# def copyclipboard():
#     random_password = pswd.get()
#     pyperclip.copy(random_password)
#     Label(tk,text="Copied to Clipboard",bg="red").pack(pady=6)

# # Label to display the primary instruction to user to enter the length of passwod he requires
# Label(tk, text="Enter the number to get password \n (Minimum length should be 8)",bg='Blue',fg='white').pack(pady=3)

# # To store the entry of user
# Entry(tk, textvariable=passlen).pack(pady=3)

# # To generate Random password and confirmation by the button click
# Button(tk, text="Generate Password", command=password_generator,bg='black',fg='white').pack(pady=7)
# Entry(tk, textvariable=pswd).pack(pady=3)

# Button(tk, text="Copy to clipboard", command=copyclipboard,bg='black',fg='white').pack()
# # To initiate and display the root window we created
# tk.mainloop()


# Import the required Module
'''import pyqrcode
import png
from pyqrcode import QRCod

# String which will be in QR
QR = "Name:- Aditya Kumar, GF:- Drishti"


# Calling the method to Generate QR code
url = pyqrcode.create(QR)

# Create and saving the png file
url.png('qrcode.png', scale = 7)