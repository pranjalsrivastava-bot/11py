from tkinter import *
import random

root=Tk()
root.title("Generate a Password")
root.geometry("400x400")

label= Label(root)

array_3d =[[['1', '2', '3', '4', '5', '6', '7', '8', '9'],["Hair", "Foot"],["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "O", "P"]]]
print(array_3d[0][2][3])

def new_password():
    random_no_1 = random.randint(0,8)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,15)
    
    letter1 =str(array_3d[0][0][random_no_1])
    letter2 =str(array_3d[0][1][random_no_2])
    letter3 =str(array_3d[0][2][random_no_3])
    label["text"] = letter1 + "" + letter2 + "" + letter3
    
    btn = Button(root, text= "New Password", command = new_password)
    btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
    root.mainloop()