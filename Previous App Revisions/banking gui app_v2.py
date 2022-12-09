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
    street_number = temp_street_number.get()
    street_name = temp_street_name.get()
    apt_number = temp_apt_number.get()
    city = temp_city.get()
    state = temp_state.get()
    zipp = temp_zipp.get()
    home_branch = temp_home_branch.get()
    role = temp_role.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if Fname == "" or Lname == "" or street_number == "" or street_name == "" or apt_number == "" or city == "" or state == "" or zipp == "" or home_branch == "" or role == "" or password == "":
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
            new_file.write(street_number+" "+street_name+" "+apt_number+'\n')
            new_file.write(city+" "+state+" "+zipp+'\n')
            new_file.write(home_branch+'\n')
            new_file.write(role+'\n')
            new_file.write('0'+'\n')
            new_file.write('null'+'\n')
            new_file.write('null')
            new_file.close()
            notif.config(fg="green",text="Account created!")
    
def register():
    #Vars
    global temp_Fname
    global temp_Lname
    global temp_street_number
    global temp_street_name
    global temp_apt_number
    global temp_city
    global temp_state
    global temp_zipp
    global temp_home_branch
    global temp_role
    global temp_password
    global notif
    
    temp_Fname = StringVar()
    temp_Lname = StringVar()
    temp_street_number = StringVar()
    temp_street_name = StringVar()
    temp_apt_number = StringVar()
    temp_city = StringVar()
    temp_state = StringVar()
    temp_zipp = StringVar()
    temp_home_branch = StringVar()
    temp_role = StringVar()
    temp_password = StringVar()
    
    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Labels
    Label(register_screen, text="Please enter your details below to register:", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="First Name", font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(register_screen, text="Last Name", font=('Times New Roman',a)).grid(row=2,sticky=W)
    Label(register_screen, text="Address", font = ('Times New Roman',a, "bold")).grid(row=3, sticky=W,pady=10)
    Label(register_screen, text="Street Number", font=('Times New Roman',a)).grid(row=4,sticky=W)
    Label(register_screen, text="Street Name", font=('Times New Roman',a)).grid(row=5,sticky=W)
    Label(register_screen, text="Apartment Number", font=('Times New Roman',a)).grid(row=6,sticky=W)
    Label(register_screen, text="City", font=('Times New Roman',a)).grid(row=7,sticky=W)
    Label(register_screen, text="State", font=('Times New Roman',a)).grid(row=8,sticky=W)
    Label(register_screen, text="ZIP Code", font=('Times New Roman',a)).grid(row=9,sticky=W)
    Label(register_screen, text="Home Banking Branch", font=('Times New Roman',a)).grid(row=10,sticky=W,pady=10)
    Label(register_screen, text="Role", font=('Times New Roman',a)).grid(row=11,sticky=W)
    Label(register_screen, text="Password", font=('Times New Roman',a)).grid(row=12,sticky=W)
    notif = Label(register_screen, font=('Times New Roman',n))
    notif.grid(row=13,sticky=N,pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_Fname).grid(row=1,column=1)
    Entry(register_screen,textvariable=temp_Lname).grid(row=2,column=1)
    Entry(register_screen,textvariable=temp_street_number).grid(row=4,column=1)
    Entry(register_screen,textvariable=temp_street_name).grid(row=5,column=1)
    Entry(register_screen,textvariable=temp_apt_number).grid(row=6,column=1)
    Entry(register_screen,textvariable=temp_city).grid(row=7,column=1)
    Entry(register_screen,textvariable=temp_state).grid(row=8,column=1)
    Entry(register_screen,textvariable=temp_zipp).grid(row=9,column=1)
    Entry(register_screen,textvariable=temp_home_branch).grid(row=10,column=1)
    Entry(register_screen,textvariable=temp_role).grid(row=11,column=1)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=12,column=1)
    
    #Buttons
    Button(register_screen, text="Register", command = finish_reg, font=('Times New Roman',b)).grid(row=14,sticky=N,pady=10)

def manager_session():
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
            role = file_data[6]
            #Account Dashboard
            if role == 'manager':
                if login_password == password:
                    login_screen.destroy()
                    account_dashboard = Toplevel(master)
                    account_dashboard.title('Manager Dashboard')
                    #Labels
                    Label(account_dashboard, text="Account Dashboard", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
                    Label(account_dashboard, text="Welcome, "+login_Fname+ " " +login_Lname + "!", font=('Times New Roman',d)).grid(row=1,sticky=N,pady=5)
                    #Buttons
                    Button(account_dashboard, text="Personal Details", font=('Times New Roman',b),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                    Button(account_dashboard, text="Account Management", font=('Times New Roman',b),width=30,command=account_management).grid(row=3,sticky=N,padx=10)                   
                    Button(account_dashboard, text="Analytics", font=('Times New Roman',b),width=30,command=analytics).grid(row=4,sticky=N,padx=10)
                    Button(account_dashboard, text="Deposit", font=('Times New Roman',b),width=30,command=deposit).grid(row=5,sticky=N,padx=10)
                    Button(account_dashboard, text="Withdraw", font=('Times New Roman',b),width=30,command=withdraw).grid(row=6,sticky=N,padx=10)
                    Button(account_dashboard, text="Transfer", font=('Times New Roman',b),width=30,command=transfer).grid(row=7,sticky=N,padx=10)
                    Button(account_dashboard, text="External Transfer", font=('Times New Roman',b),width=30,command=external_transfer).grid(row=8,sticky=N,padx=10)                    
                    Label(account_dashboard).grid(row=9,sticky=N,pady=10)
                    return
                else:
                    login_notif.config(fg="red", text="Password incorrect!")
                    return
            else:
                login_notif.config(fg="red", text="Access denied, not a manager.")
                return
        login_notif.config(fg="red", text="No account found!")
        
def loan_manager_session():
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
            role = file_data[6]
            #Account Dashboard
            if role == 'loan manager':
                if login_password == password:
                    login_screen.destroy()
                    account_dashboard = Toplevel(master)
                    account_dashboard.title('Loan Manager Dashboard')
                    #Labels
                    Label(account_dashboard, text="Account Dashboard", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
                    Label(account_dashboard, text="Welcome, "+login_Fname+ " " +login_Lname + "!", font=('Times New Roman',d)).grid(row=1,sticky=N,pady=5)
                    #Buttons
                    Button(account_dashboard, text="Personal Details", font=('Times New Roman',b),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                    Button(account_dashboard, text="Deposit", font=('Times New Roman',b),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                    Button(account_dashboard, text="Withdraw", font=('Times New Roman',b),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
                    Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                    return
                else:
                    login_notif.config(fg="red", text="Password incorrect!")
                    return
            else:
                login_notif.config(fg="red", text="Access denied, not a loan manager.")
                return
        login_notif.config(fg="red", text="No account found!")

def teller_session():
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
            role = file_data[6]
            #Account Dashboard
            if role == 'teller':
                if login_password == password:
                    login_screen.destroy()
                    account_dashboard = Toplevel(master)
                    account_dashboard.title('Teller Dashboard')
                    #Labels
                    Label(account_dashboard, text="Account Dashboard", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
                    Label(account_dashboard, text="Welcome, "+login_Fname+ " " +login_Lname + "!", font=('Times New Roman',d)).grid(row=1,sticky=N,pady=5)
                    #Buttons
                    Button(account_dashboard, text="Personal Details", font=('Times New Roman',b),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                    Button(account_dashboard, text="Deposit", font=('Times New Roman',b),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                    Button(account_dashboard, text="Withdraw", font=('Times New Roman',b),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
                    Button(account_dashboard, text="Transfer", font=('Times New Roman',b),width=30,command=transfer).grid(row=5,sticky=N,padx=10)
                    Button(account_dashboard, text="External Transfer", font=('Times New Roman',b),width=30,command=external_transfer).grid(row=6,sticky=N,padx=10)                    
                    Label(account_dashboard).grid(row=7,sticky=N,pady=10)
                    return
                else:
                    login_notif.config(fg="red", text="Password incorrect!")
                    return
            else:
                login_notif.config(fg="red", text="Access denied, not a teller.")
                return
        login_notif.config(fg="red", text="No account found!")
                
def customer_session():
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
            role = file_data[6]
            #Account Dashboard
            if role == 'customer':
                if login_password == password:
                    login_screen.destroy()
                    account_dashboard = Toplevel(master)
                    account_dashboard.title('Customer Dashboard')
                    #Labels
                    Label(account_dashboard, text="Account Dashboard", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
                    Label(account_dashboard, text="Welcome, "+login_Fname+ " " +login_Lname + "!", font=('Times New Roman',d)).grid(row=1,sticky=N,pady=5)
                    #Buttons
                    Button(account_dashboard, text="Personal Details", font=('Times New Roman',b),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                    Button(account_dashboard, text="Personal Account Management", font=('Times New Roman',b),width=30,command=personal_account_management).grid(row=3,sticky=N,padx=10)                   
                    Button(account_dashboard, text="Deposit", font=('Times New Roman',b),width=30,command=deposit).grid(row=4,sticky=N,padx=10)
                    Button(account_dashboard, text="Withdraw", font=('Times New Roman',b),width=30,command=withdraw).grid(row=5,sticky=N,padx=10)
                    Button(account_dashboard, text="Transfer", font=('Times New Roman',b),width=30,command=transfer).grid(row=6,sticky=N,padx=10)
                    Button(account_dashboard, text="External Transfer", font=('Times New Roman',b),width=30,command=external_transfer).grid(row=7,sticky=N,padx=10)                    
                    Label(account_dashboard).grid(row=8,sticky=N,pady=10)
                    return
                else:
                    login_notif.config(fg="red", text="Password incorrect!")
                    return
            else:
                login_notif.config(fg="red", text="Access denied, not a customer.")
                return
        login_notif.config(fg="red", text="No account found!")

def analytics():
    print("analytics")

def account_management():
    #Vars
    global temp_entered_Fname
    global temp_entered_Lname
    global account_notif
    global account_management_screen
    temp_entered_Fname = StringVar()
    temp_entered_Lname = StringVar()
    #Account Selection Screen
    account_selection = Toplevel(master)
    account_selection.title('Account Management')
    #Labels
    Label(account_selection, text="Enter Account Name", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    Label(account_selection, text="First Name", font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(account_selection, text="Last Name", font=('Times New Roman',a)).grid(row=2,sticky=W)
    #Entry
    Entry(account_selection, textvariable=temp_entered_Fname).grid(row=1,column=1,padx=5)
    Entry(account_selection, textvariable=temp_entered_Lname).grid(row=2,column=1,padx=5)
    #Button
    Button(account_selection, text="Enter", command=account, width=15,font=('Times New Roman',t)).grid(row=4,sticky=W,pady=5,padx=5)

def account():
    all_accounts = os.listdir()
    entered_Fname = temp_entered_Fname.get()
    entered_Lname = temp_entered_Lname.get()

    for fullName in all_accounts:
        if entered_Fname + "_" + entered_Lname == fullName:
            file = open(entered_Fname + "_" + entered_Lname,"r")
            file_data = file.read()
            user_acc = file_data.split('\n')
            acc_name = user_acc[0] + " " + user_acc[1]
            acc_month_statement = user_acc[8]
            acc_pending_transactions = user_acc[9]
            acc_balance = user_acc[7]
            #Account Management screen
            account_management = Toplevel(master)
            account_management.title('Account Management')
            #Labels
            Label(account_management, text="Account Management for: " + acc_name, font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10,padx=10)
            Label(account_management, text="Name: "+acc_name, font=('Times New Roman',a)).grid(row=1,sticky=W)
            Label(account_management, text="Monthly Statement: "+acc_month_statement, font=('Times New Roman',a)).grid(row=2,sticky=W)
            Label(account_management, text="Pending Transactions: "+acc_pending_transactions, font=('Times New Roman',a)).grid(row=4,sticky=W)
            Label(account_management, text="Balance: $"+acc_balance, font=('Times New Roman',a)).grid(row=5,sticky=W)
            #Buttons
            Button(account_management, text="Interest",command=interest,width=15,font=('Times New Roman',b)).grid(row=6,sticky=N,pady=5)
            Button(account_management, text="Overdraft Fees",command=overdraft_fees,width=15,font=('Times New Roman',b)).grid(row=7,sticky=N)
            Button(account_management, text="Account Fees",command=account_fees,width=15,font=('Times New Roman',b)).grid(row=8,sticky=N,pady=5)

def interest():
    print("interest")
def overdraft_fees():
    print("overdraft_fees")
def account_fees():
    print("account_fees")
            
def personal_account_management():
    #Vars
    file = open(login_Fname + "_" + login_Lname, 'r')
    file_data = file.read()
    user_accman = file_data.split('\n')
    accman_name = user_accman[0] + " " + user_accman[1]
    accman_month_statement = user_accman[8]
    accman_pending_transactions = user_accman[9]
    accman_balance = user_accman[7]
    #Personal Account Management screen
    personal_account_management = Toplevel(master)
    personal_account_management.title('Personal Account Management')
    #Labels
    Label(personal_account_management, text="Personal Account Management", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
    Label(personal_account_management, text="Name: "+accman_name, font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(personal_account_management, text="Monthly Statement: "+accman_month_statement, font=('Times New Roman',a)).grid(row=2,sticky=W)
    Label(personal_account_management, text="Pending Transactions: "+accman_pending_transactions, font=('Times New Roman',a)).grid(row=4,sticky=W)
    Label(personal_account_management, text="Balance: $"+accman_balance, font=('Times New Roman',a)).grid(row=5,sticky=W)
    #Buttons
    Button(personal_account_management, text="Create Account", font=('Times New Roman',b),width=30,command=create_account).grid(row=7,sticky=N,pady=10)
    Button(personal_account_management, text="Delete Account", font=('Times New Roman',b),width=30,command=delete_account).grid(row=8,sticky=N,pady=10) 

def create_account():
    print("create account")

def delete_account():
    print("delete account")

def deposit():
    print("deposit")
    #global deposit_value
    #deposit_value = temp_deposit_value.get()
    #Label(register_screen, text="Enter deposit amount below:", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    #Entry(register_screen,textvariable=temp_deposit_value).grid(row=1,sticky=N)
    #file = open(login_Fname + "_" + login_Lname,"r")
    #file_data = file.read()
    #file_data = file_data.split('\n')
    
def withdraw():
    print("withdraw")

def transfer():
    print("transfer")

def external_transfer():
    print("external transfer")
    
def personal_details():
    #Vars
    file = open(login_Fname + "_" + login_Lname, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0] + " " + user_details[1]
    details_address = user_details[3]+ "\n" +user_details[4]
    details_home_branch = user_details[5]
    details_role = user_details[6]
    details_balance = user_details[7]
    #Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    #Labels
    Label(personal_details_screen, text="Personal Details", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen, text="Name: "+details_name, font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(personal_details_screen, text="Address: "+details_address, font=('Times New Roman',a)).grid(row=2,sticky=W)
    Label(personal_details_screen, text="Branch: "+details_home_branch, font=('Times New Roman',a)).grid(row=4,sticky=W)
    Label(personal_details_screen, text="Role: "+details_role, font=('Times New Roman',a)).grid(row=5,sticky=W)
    Label(personal_details_screen, text="Balance: $"+details_balance, font=('Times New Roman',a)).grid(row=6,sticky=W)       

def role():
    #Role Selection Screen
    role_screen = Toplevel(master)
    role_screen.title('Role')
    #Labels
    Label(role_screen,text="Select your role",font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    #Buttons
    Button(role_screen,text="Manager",command=manager_login,width=15,font=('Times New Roman',t)).grid(row=4,sticky=W,pady=5,padx=5)
    Button(role_screen,text="Loan Manager",command=loan_manager_login,width=15,font=('Times New Roman',t)).grid(row=5,sticky=W,pady=5,padx=5)
    Button(role_screen,text="Teller",command=teller_login,width=15,font=('Times New Roman',t)).grid(row=6,sticky=W,pady=5,padx=5)
    Button(role_screen,text="Customer",command=customer_login,width=15,font=('Times New Roman',t)).grid(row=7,sticky=W,pady=5,padx=5)
    
def manager_login():
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
    login_screen.title('Manager Login')
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
    Button(login_screen, text="Login", command=manager_session, width=15,font=('Times New Roman',t)).grid(row=4,sticky=W,pady=5,padx=5)
def loan_manager_login():
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
    login_screen.title('Loan Manager Login')
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
    Button(login_screen, text="Login", command=loan_manager_session, width=15,font=('Times New Roman',t)).grid(row=4,sticky=W,pady=5,padx=5)

def teller_login():
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
    login_screen.title('Teller Login')
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
    Button(login_screen, text="Login", command=teller_session, width=15,font=('Times New Roman',t)).grid(row=4,sticky=W,pady=5,padx=5)


def customer_login():
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
    login_screen.title('Customer Login')
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
    Button(login_screen, text="Login", command=customer_session, width=15,font=('Times New Roman',t)).grid(row=4,sticky=W,pady=5,padx=5)

#Labels
Label(master, text = "Custom Banking Beta GUI", font=('Times New Roman', 30)).grid(row=0,sticky=N,pady=5,padx=30)
Label(master, text = "made by Group 1: Akina C., Ana S., Julia I.", font=('Times New Roman', d)).grid(row=1,sticky=N,pady=5)

#Buttons
Button(master, text="Register", font=('Times New Roman', b),width=20,command=register).grid(row=3,sticky=N)
Button(master, text="Login", font=('Times New Roman', b),width=20,command=role).grid(row=4,sticky=N,pady=10)

master.mainloop()

