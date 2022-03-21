import mysql.connector as pymysql
import smtplib
from tkinter import *
root = Tk()
root.geometry("1100x355")

def send():
    user = uservalue.get()
    pasw = passvalue.get()
    sender = sendervalue.get()
    msg = messagevalue.get()

    conn = pymysql.connect(host="localhost",
                           user="root",
                           passwd="",
                           db="students_insformation"
                           )
    cursor = conn.cursor()
    query = "SELECT gmail FROM students_insformation "
    cursor.execute(query)
    usernames = cursor.fetchall()

    for username in usernames:
        s = ''.join(username)
        to = s
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(user, pasw)
        server.sendmail(sender, to, msg)
        server.quit()
        print("done")








titale = Label(text="Advance Mail System").grid(row=0,column=3)


user=Label(root,text="Email",font=("comicsansms", 10, "bold")).grid(row=1,column=0)
uservalue=StringVar()
userentery =Entry(root,textvariable = uservalue,font=("comicsansms", 10, "bold"),width=40).grid(row=1,column=1)


password=Label(root,text="password",font=("comicsansms", 10, "bold")).grid(row=1,column=2)
passvalue=StringVar()
passentery =Entry(root,textvariable = passvalue,font=("comicsansms", 10, "bold"),width=40).grid(row=1,column=3)



sender=Label(root,text="Sender",font=("comicsansms", 10, "bold")).grid(row=2,column=0)
sendervalue=StringVar()
senderentery =Entry(root,textvariable = sendervalue,font=("comicsansms", 10, "bold"),width=40).grid(row=2,column=1)


to=Label(root,text="To",font=("comicsansms", 10, "bold")).grid(row=2,column=2)
tovalue=StringVar()
toentery =Entry(root,textvariable = tovalue,font=("comicsansms", 10, "bold"),width=40).grid(row=2,column=3)


message=Label(root,text="Massage",font=("comicsansms", 10, "bold")).grid(row=2,column=4)
messagevalue=StringVar()
messageentery =Entry(root,textvariable = messagevalue,width=40,font=("comicsansms", 10, "bold")).grid(row=2,column=5)


Button(text="Send",bg="red",fg="white",padx=10,pady=0,font =("comicsansms",10,"bold"),relief=SUNKEN,borderwidth=5,command=send).grid(row=2,column=6)

root.mainloop()