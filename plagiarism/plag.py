import difflib
from tkinter import *
import time
from PIL import ImageTk,Image
from tkinter import messagebox
def check_plagiarism():
    file1 = text.get("1.0", "end-1c")
    file2 = text2.get("1.0", "end-1c")
    if file1=="" or file2=="" or file1=="Paste Your Text Here!!!!" or file2=="Paste Your Text Here!!!!":
        messagebox.showwarning("PLAGIARISM","Please Enter The Text")
    else:
        similarity = difflib.SequenceMatcher(None, file1, file2)
        result = similarity.ratio() * 100
        time.sleep(2)
        text.delete(1.0, "end")
        text.insert("end", "wait checking ...........")
        time.sleep(5)
        messagebox.showinfo("Sucess", result)

root=Tk()
root.geometry("900x700")
root.title("Plagiarism checker")
bg1=PhotoImage(file='ball.png')
ab=Label(root,image=bg1,bd=0).place(x=0,y=0,relwidth=1)
header = Label(root,bg="black",width="300",height="4")
header.place(x=0,y=0)
logo = ImageTk.PhotoImage(Image.open("loog.png"))
b = Label(root,image=logo,borderwidth=0)
b.place(x=10,y=10)
tit=Label(root,text="plagiarism checker",font=("Microsoft YaHei UI","15","bold"),bg="black",fg="white")
tit.place(x=43,y=14)
text = Text(root,width=80,height=15,font=("","10","bold"),borderwidth=4,relief="raised",pady=10)
text.place(x=20,y=180)
text.insert("end","Paste Your Text Here!!!!")
text2 = Text(root,width=80,height=15,font=("","10","bold"),borderwidth=4,relief="raised",pady=10 )
text2.place(x=660,y=180)
text2.insert("end","Paste Your Text Here!!!!")
button = Button(root,command=check_plagiarism,text="Check",relief=RIDGE,font=("","20","bold"),bg="black",fg="white")
button.place(x=550,y=500)


root.mainloop()