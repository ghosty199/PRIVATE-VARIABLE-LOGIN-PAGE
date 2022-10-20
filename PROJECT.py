from tkinter import*
import random
root=Tk()
from PIL import Image, ImageTk
from tkinter import ttk
root.geometry("1000x1000")
root.title("Encapsulation")

label5=Label(root, text="name", fg="black",font=("times",20))
label5.place(relx=0.2, rely=0.1, anchor=CENTER)

label6=Label(root, text="password", fg="black",font=("times",20))
label6.place(relx=0.2, rely=0.2, anchor=CENTER)

label7=Label(root, text="captcha", fg="black",font=("times",20))
label7.place(relx=0.2, rely=0.3, anchor=CENTER)


label8=Label(root, text="", fg="black",font=("times",20))
label8.place(relx=0.2, rely=0.8, anchor=CENTER)


label9=Label(root, text="", fg="black",font=("times",20))
label9.place(relx=0.2, rely=0.85, anchor=CENTER)


label10=Label(root, text="", fg="black",font=("times",20))
label10.place(relx=0.2, rely=0.9, anchor=CENTER)


inputname=Entry(root)
inputname.place(relx=0.4,rely=0.1, anchor=CENTER)


inputcaptcha=Entry(root)
inputcaptcha.place(relx=0.4,rely=0.2, anchor=CENTER)


inputpassword=Entry(root)
inputpassword.place(relx=0.4,rely=0.3, anchor=CENTER)


class UserDetails():
    def __init__(self):
        self.__name="hi"
        self.__password="nxqbv29505"
        self.captcha="hello199"
    def updateDetails(self):
        label8["text"]=self.__name
        label9["text"]=self.__password
        label10["text"]=self.captcha 
    
object1=UserDetails()


def addUser():
    global object1
    object1.name=inputname.get()
    object1.password=inputpassword.get()
    object1.captcha=inputcaptcha.get()
     

button1=Button(root,text="update login details",command=addUser)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)

    

button2=Button(root,text="show profile",command=object1.updateDetails)
button2.place(relx=0.5, rely=0.4, anchor=CENTER)








root.mainloop()