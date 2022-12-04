#imports
from tkinter import *
import os

#Main Screen
master = Tk()
master.title('Banking System Application')

#Functions
d = 20 # font size for descriptions
n = 14 # font size for notifs
a = 16 # font size for attributes
t = 24 # font size for titles
b = 18 # font size for buttons


def finish_reg():
    Fname = temp_Fname.get()
    Lname = temp_Lname.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if Fname == "" or Lname == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red",text="All fields required * ")
        return

    for name_check in all_accounts:
        if Fname + "_" + Lname == name_check:
            notif.config(fg="red",text="Account already exists")
            return
        else:
            new_file = open(Fname + "_" + Lname,"w")
            new_file.write(Fname + '\n')
            new_file.write(Lname +'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green",text="Account created!")
    
def register():
    #Vars
    global temp_Fname
    global temp_Lname
    global temp_age
    global temp_gender
    global temp_password
    global notif
    
    temp_Fname = StringVar()
    temp_Lname = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Labels
    Label(register_screen, text="Please enter your details below to register:", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="First Name", font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(register_screen, text="Last Name", font=('Times New Roman',a)).grid(row=2,sticky=W)
    Label(register_screen, text="Age", font=('Times New Roman',a)).grid(row=3,sticky=W)
    Label(register_screen, text="Gender", font=('Times New Roman',a)).grid(row=4,sticky=W)
    Label(register_screen, text="Password", font=('Times New Roman',a)).grid(row=5,sticky=W)
    notif = Label(register_screen, font=('Times New Roman',n))
    notif.grid(row=6,sticky=N,pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_Fname).grid(row=1,column=1)
    Entry(register_screen,textvariable=temp_Lname).grid(row=2,column=1)
    Entry(register_screen,textvariable=temp_age).grid(row=3,column=1)
    Entry(register_screen,textvariable=temp_gender).grid(row=4,column=1)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=5,column=1)
    
    #Buttons
    Button(register_screen, text="Register", command = finish_reg, font=('Times New Roman',b)).grid(row=8,sticky=N,pady=10)

def login_session():
    global login_Fname
    global login_Lname
    all_accounts = os.listdir()
    login_Fname = temp_login_Fname.get()
    login_Lname = temp_login_Lname.get()
    login_password = temp_login_password.get()

    for fullName in all_accounts:
        if login_Fname + "_" + login_Lname == fullName:
            file = open(login_Fname + "_" + login_Lname,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[2]
            #Account Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')
                #Labels
                Label(account_dashboard, text="Account Dashboard", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome "+login_Fname+ " " +login_Lname, font=('Times New Roman',t)).grid(row=1,sticky=N,pady=5)
                #Buttons
                Button(account_dashboard, text="Personal Details", font=('Times New Roman',b),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard, text="Deposit", font=('Times New Roman',b),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard, text="Withdraw", font=('Times New Roman',b),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="red", text="Password incorrect!")
                return
        login_notif.config(fg="red", text="No account found!")

def deposit():
    print("deposit")
def withdraw():
    print("withdraw")
def personal_details():
    #Vars
    file = open(login_Fname + "_" + login_Lname, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0] + " " + user_details[1]
    details_age = user_details[3]
    details_gender = user_details[4]
    details_balance = user_details[5]
    #Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    #Labels
    Label(personal_details_screen, text="Personal Details", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen, text="Name: "+details_name, font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(personal_details_screen, text="Age: "+details_age, font=('Times New Roman',a)).grid(row=2,sticky=W)
    Label(personal_details_screen, text="Gender: "+details_gender, font=('Times New Roman',a)).grid(row=3,sticky=W)
    Label(personal_details_screen, text="Balance: $"+details_balance, font=('Times New Roman',a)).grid(row=4,sticky=W)
    
    
    
def login():
    #Vars
    global temp_login_Fname
    global temp_login_Lname
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_Fname = StringVar()
    temp_login_Lname = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    #Labels
    Label(login_screen, text="Login to your account", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="First Name", font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(login_screen, text="Last Name", font=('Times New Roman',a)).grid(row=2,sticky=W)
    Label(login_screen, text="Password", font=('Times New Roman',a)).grid(row=3,sticky=W)
    login_notif = Label(login_screen, font=('Times New Roman',n))
    login_notif.grid(row=5,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_Fname).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_Lname).grid(row=2,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=3,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=login_session, width=15,font=('Times New Roman',t)).grid(row=4,sticky=W,pady=5,padx=5)

#Labels
Label(master, text = "Custom Banking Beta GUI", font=('Times New Roman', 30)).grid(row=0,sticky=N,pady=5,padx=30)
Label(master, text = "made by Group 1: Akina C., Ana S., Julia I.", font=('Times New Roman', d)).grid(row=1,sticky=N,pady=5)

#Buttons
Button(master, text="Register", font=('Times New Roman', b),width=20,command=register).grid(row=3,sticky=N)
Button(master, text="Login", font=('Times New Roman', b),width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()

