#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


objects = dir()

for obj in objects:
    del globals()[obj]


#imports
from tkinter import *
import os
import psycopg2
#from PIL import ImageTk, Image  


conn = psycopg2.connect(user="postgres",
                                  password="Kirbygenius2022",
                                  host="localhost",
                                  port="5433",
                                  database="bankingsystem")

cur = conn.cursor()

#Main Screen
master = Tk()
master.title('Banking System Application')
master.configure(bg='pink')

#Image Import
#img = Image.open('piggy.png')
#img = img.resize((150,150))
#img = ImageTk.PhotoImage(img)

#Functions
d = 20 # font size for descriptions
n = 14 # font size for notifs
a = 16 # font size for attributes
t = 24 # font size for titles
b = 18 # font size for buttons


def finish_reg():
    SSN_input = temp_SSN.get()
    Fname = temp_Fname.get()
    Lname = temp_Lname.get()
    street_number = temp_street_number.get()
    street_name = temp_street_name.get()
    apt_number = temp_apt_number.get()
    city = temp_city.get()
    state = temp_state.get()
    zipp = temp_zipp.get()
    home_branch = temp_home_branch.get()
    #password = temp_password.get()
    all_accounts = os.listdir()

    if SSN_input == "" or Fname == "" or Lname == "" or street_number == "" or street_name == "" or city == "" or state == "" or zipp == "" or home_branch == "" :
        notif.config(fg="red",text="All fields required * ")
        return
    
    try:  
        cur.execute(f"INSERT INTO  customer VALUES('{SSN_input}', '{Fname}', '{Lname}', '{street_number}', '{street_name}', '{apt_number}', '{city}', '{state}', '{zipp}', '{home_branch}')")
        conn.commit()
        notif.config(fg="green",text="New customer added!")
    
    except psycopg2.errors.UniqueViolation:
        notif.config(fg="red",text="Existing customer!")
    
def register():
    #Vars
    global temp_SSN
    global temp_Fname
    global temp_Lname
    global temp_street_number
    global temp_street_name
    global temp_apt_number
    global temp_city
    global temp_state
    global temp_zipp
    global temp_home_branch
    #global temp_password
    global notif
    
    temp_SSN = StringVar()
    temp_Fname = StringVar()
    temp_Fname = StringVar()
    temp_Lname = StringVar()
    temp_street_number = StringVar()
    temp_street_name = StringVar()
    temp_apt_number = StringVar()
    temp_city = StringVar()
    temp_state = StringVar()
    temp_zipp = StringVar()
    temp_home_branch = StringVar()
    #temp_password = StringVar()
    
    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title('New Customer')

    #Labels
    Label(register_screen, text="Please enter your details below to register:", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="SSN", font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(register_screen, text="First Name", font=('Times New Roman',a)).grid(row=2,sticky=W)
    Label(register_screen, text="Last Name", font=('Times New Roman',a)).grid(row=3,sticky=W)
    Label(register_screen, text="Address", font = ('Times New Roman',a, "bold")).grid(row=4, sticky=W,pady=10)
    Label(register_screen, text="Street Number", font=('Times New Roman',a)).grid(row=5,sticky=W)
    Label(register_screen, text="Street Name", font=('Times New Roman',a)).grid(row=6, sticky=W)
    Label(register_screen, text="Apartment Number", font=('Times New Roman',a)).grid(row=7,sticky=W)
    Label(register_screen, text="City", font=('Times New Roman',a)).grid(row=8,sticky=W)
    Label(register_screen, text="State", font=('Times New Roman',a)).grid(row=9,sticky=W)
    Label(register_screen, text="ZIP Code", font=('Times New Roman',a)).grid(row=10,sticky=W)
    Label(register_screen, text="Home Banking Branch", font=('Times New Roman',a)).grid(row=11,sticky=W,pady=10)
    #Label(register_screen, text="Password", font=('Times New Roman',a)).grid(row=12,sticky=W)
    notif = Label(register_screen, font=('Times New Roman',n))
    notif.grid(row=13,sticky=N,pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_SSN).grid(row=1,column=1)
    Entry(register_screen,textvariable=temp_Fname).grid(row=2,column=1)
    Entry(register_screen,textvariable=temp_Lname).grid(row=3,column=1)
    Entry(register_screen,textvariable=temp_street_number).grid(row=5,column=1)
    Entry(register_screen,textvariable=temp_street_name).grid(row=6,column=1)
    Entry(register_screen,textvariable=temp_apt_number).grid(row=7,column=1)
    Entry(register_screen,textvariable=temp_city).grid(row=8,column=1)
    Entry(register_screen,textvariable=temp_state).grid(row=9,column=1)
    Entry(register_screen,textvariable=temp_zipp).grid(row=10,column=1)
    Entry(register_screen,textvariable=temp_home_branch).grid(row=11,column=1)
    #Entry(register_screen,textvariable=temp_password,show="*").grid(row=12,column=1)
    
    #Buttons
    Button(register_screen, text="Register", command = finish_reg, font=('Times New Roman',b)).grid(row=14,sticky=N,pady=10)

def manager_session():
    #assume managers are already in the system
    #identify by SSN
    
    global manager_login_SSN

    manager_login_SSN = temp_login_SSN.get()
 
    cur.execute(f"SELECT employee_type FROM employee WHERE SSN='{manager_login_SSN}'")
    conn.commit()
    employee_type_t = cur.fetchall()
    employee_type = employee_type_t[0]
    #login_notif.config(fg="red", text=employee_type)
    
    cur.execute(f"SELECT first_name FROM employee WHERE SSN='{manager_login_SSN}'")
    conn.commit()
    firstName = cur.fetchall()
    Fname = ''.join(firstName[0])
    
    cur.execute(f"SELECT last_name FROM employee WHERE SSN='{manager_login_SSN}'")
    conn.commit()
    lastName = cur.fetchall()
    Lname = ''.join(lastName[0])

  
    if employee_type[0] == 'manager':
        #Account Dashboard
        login_screen.destroy()
        account_dashboard = Toplevel(master)
        account_dashboard.title('Manager Dashboard')
        #Labels
        Label(account_dashboard, text="Account Dashboard", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
        Label(account_dashboard, text="Welcome, "+Fname+ " " +Lname + "!", font=('Times New Roman',d)).grid(row=1,sticky=N,pady=5)
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
        login_notif.config(fg="red", text="Access denied, not a manager.")
        return
  
  
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
     #assume managers are already in the system
    #identify by SSN
    
    global login_SSN

    login_SSN = temp_login_SSN.get()
 
    cur.execute(f"SELECT employee_type FROM employee WHERE SSN='{login_SSN}'")
    conn.commit()
    employee_type_t = cur.fetchall()
    employee_type = employee_type_t[0]
    #login_notif.config(fg="red", text=employee_type)
    
    cur.execute(f"SELECT first_name FROM employee WHERE SSN='{login_SSN}'")
    conn.commit()
    firstName = cur.fetchall()
    Fname = ''.join(firstName[0])
    
    cur.execute(f"SELECT last_name FROM employee WHERE SSN='{login_SSN}'")
    conn.commit()
    lastName = cur.fetchall()
    Lname = ''.join(lastName[0])
  
    if employee_type[0] == 'teller':
        #Account Dashboard
        login_screen.destroy()
        account_dashboard = Toplevel(master)
        account_dashboard.title('Teller Dashboard')
        #Labels
        Label(account_dashboard, text="Account Dashboard", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
        Label(account_dashboard, text="Welcome, "+Fname+ " " +Lname + "!", font=('Times New Roman',d)).grid(row=1,sticky=N,pady=5)
        #Buttons
        Button(account_dashboard, text="Personal Details", font=('Times New Roman',b),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
        Button(account_dashboard, text="Deposit", font=('Times New Roman',b),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
        Button(account_dashboard, text="Withdraw", font=('Times New Roman',b),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
        Button(account_dashboard, text="Transfer", font=('Times New Roman',b),width=30,command=transfer).grid(row=5,sticky=N,padx=10)
        Button(account_dashboard, text="External Transfer", font=('Times New Roman',b),width=30,command=external_transfer).grid(row=6,sticky=N,padx=10)                    
        Label(account_dashboard).grid(row=7,sticky=N,pady=10)
        return
    else:
        login_notif.config(fg="red", text="Access denied, not a teller.")
        return
                
def customer_session():
    global login_Fname
    global login_Lname
    global ssn_cust
    login_Fname = temp_login_Fname.get()
    login_Lname = temp_login_Lname.get()
    ssn_cust = temp_login_SSN.get()
    conn.commit()
    login_screen.destroy()
    account_dashboard = Toplevel(master)
    account_dashboard.title('Customer Dashboard')
    #Labels
    Label(account_dashboard, text="Account Dashboard", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
    Label(account_dashboard, text="Welcome, "+login_Fname+ " " +login_Lname + "!", font=('Times New Roman',d)).grid(row=1,sticky=N,pady=5)
    #Buttons
    Button(account_dashboard, text="Personal Details", font=('Times New Roman',b),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
    Button(account_dashboard, text="Personal Account Management", font=('Times New Roman',b),width=30,command=personal_account_management).grid(row=3,sticky=N,padx=10)                   
    Button(account_dashboard, text="Deposit", font=('Times New Roman',b),width=30,command=toDeposit).grid(row=4,sticky=N,padx=10)
    Button(account_dashboard, text="Withdraw", font=('Times New Roman',b),width=30,command=withdraw).grid(row=5,sticky=N,padx=10)
    Button(account_dashboard, text="Transfer", font=('Times New Roman',b),width=30,command=transfer).grid(row=6,sticky=N,padx=10)
    Button(account_dashboard, text="External Transfer", font=('Times New Roman',b),width=30,command=external_transfer).grid(row=7,sticky=N,padx=10)   
    #Button(account_dashboard, text="Analytics", font=('Times New Roman',b),width=30,command=analytics).grid(row=8,sticky=N,padx=10) 
    Label(account_dashboard).grid(row=9,sticky=N,pady=10)
   # if 
       # login_notif.config(fg="red", text="Password incorrect!")
    #return
           # else:
              #  login_notif.config(fg="red", text="Access denied, not a customer.")
               # return
       # login_notif.config(fg="red", text="No account found!")

def analytics():
    #Vars
    global temp_branch_selection
    global branch_selection
    
    temp_branch_selection = StringVar()

    branch_selection = Toplevel(master)
    branch_selection.title('Branch Analytics')
    #Labels
    Label(branch_selection, text="Enter branch number or click all branches", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    #Entry
    Entry(branch_selection, textvariable=temp_branch_selection).grid(row=1,sticky=N,padx=5)
    #Button
    Button(branch_selection, text="Enter", command=one_branch_analytics, width=15,font=('Times New Roman',t)).grid(row=2,sticky=W,pady=5,padx=5)
    Button(branch_selection, text="All branches", command=all_branch_analytics, width=15,font=('Times New Roman',t)).grid(row=3,sticky=W,pady=5,padx=5)

def one_branch_analytics():
    branch = temp_branch_selection.get()
    cur.execute(f"SELECT sum(balance) FROM account3 where branch_account = '{branch}'")
    conn.commit()
    net_worth_1 = cur.fetchall()
    net_worth = net_worth_1[0]
    notif = Label(branch_selection, font=('Times New Roman',n))
    notif.grid(row=6,sticky=N,pady=10)
    notif.config(fg="green",text=net_worth)
    

    
def all_branch_analytics():
    cur.execute("SELECT sum(balance) FROM account3")
    conn.commit()
    net_worth_1 = cur.fetchall()
    net_worth = net_worth_1[0]
    notif = Label(branch_selection, font=('Times New Roman',n))
    notif.grid(row=6,sticky=N,pady=10)
    notif.config(fg="green",text=net_worth)

def account_management():
    #Vars
    global temp_SSN
    global account_notif
    global account_management_screen
    temp_SSN = StringVar()
    #Account Selection Screen
    account_selection = Toplevel(master)
    account_selection.title('Account Management')
    #Labels
    Label(account_selection, text="Enter Account SSN", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    #Entry
    Entry(account_selection, textvariable=temp_SSN).grid(row=1,sticky=N,padx=5)
    #Button
    Button(account_selection, text="Enter", command=account, width=15,font=('Times New Roman',t)).grid(row=2,sticky=W,pady=5,padx=5)

def account():
    global SSN
    SSN = temp_SSN.get()
    cur.execute(f"SELECT ssn FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    
    cur.execute(f"SELECT first_name FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    firstName = cur.fetchall()
    Fname = ''.join(firstName[0])
    
    cur.execute(f"SELECT last_name FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    lastName = cur.fetchall()
    Lname = ''.join(lastName[0])
    
    #monthly statement
    cur.execute(f"SELECT monthly_statement FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    ms = cur.fetchall()
    monthly_statement = ''.join(ms[0])
    
    #pending transactions
    cur.execute(f"SELECT pending_transaction FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    pt = cur.fetchall()
    pending_transactions = ''.join(pt[0])
    
    #balance
    cur.execute(f"SELECT balance FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    b = cur.fetchall()
    bal = b[0]
    balance = str(bal[0])

    #Account Management screen
    account_management = Toplevel(master)
    account_management.title('Account Management')
    #Labels
    Label(account_management, text="Account Management for: " + Fname + " " + Lname, font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10,padx=10)
    Label(account_management, text="Name: "+ Fname + " " + Lname, font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(account_management, text="Monthly Statement: "+monthly_statement, font=('Times New Roman',a)).grid(row=2,sticky=W)
    Label(account_management, text="Pending Transactions: "+pending_transactions, font=('Times New Roman',a)).grid(row=4,sticky=W)
    Label(account_management, text="Balance: $"+balance, font=('Times New Roman',a)).grid(row=5,sticky=W)
    #Buttons
    Button(account_management, text="Interest",command=interest,width=15,font=('Times New Roman',b)).grid(row=6,sticky=N,pady=5)
    Button(account_management, text="Overdraft Fees",command=overdraft_fees,width=15,font=('Times New Roman',b)).grid(row=7,sticky=N)
    Button(account_management, text="Account Fees",command=account_fees,width=15,font=('Times New Roman',b)).grid(row=8,sticky=N,pady=5)

def interest():
    global temp_intRate
    temp_intRate = StringVar()
    #Interest screen
    interest_screen = Toplevel(master)
    interest_screen.title('Interest')
    #Label
    Label(interest_screen,text="Enter Interest Rate to Add:(enter in form 1.__)",font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    #Entry
    Entry(interest_screen, textvariable=temp_intRate).grid(row=1,sticky=N,padx=5)
    #Button
    Button(interest_screen,text="Enter",command=interestCalc,width=15,font=('Times New Roman',b)).grid(row=3,sticky=N,pady=5)
def interestCalc():
    #Interest Added Confirmation Screen
    global intRatestr
    global intRate
    intRatestr = str(temp_intRate.get())
    intRate = float(temp_intRate.get())
    interest = intRate
    
    cur.execute(f"SELECT balance FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    b = cur.fetchone()
    bal = float(b[0])
    
    newbal = int(bal * interest)
    cur.execute(f"UPDATE customer SET balance='{newbal}' WHERE SSN='{SSN}'")
    cur.execute(f"SELECT balance FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    nb = cur.fetchone()
    nbal = str(nb[0])
    
    interest_conf = Toplevel(master)
    interest_conf.title('Interest')
    Label(interest_conf,text="The Following Interest Rate Was Added:(%)" + intRatestr,font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    Label(interest_conf,text="The New Current Balance is: $" + nbal,font=('Times New Roman',d)).grid(row=1,sticky=N)
    Button(interest_conf,text="Return to Account Management",command=account_management,width=30,font=('Times New Roman',b)).grid(row=2,sticky=N,pady=5)
    
def overdraft_fees():
    global temp_odfee
    temp_odfee = StringVar()
    #Overdraft Fees screen
    overdraftfees_screen = Toplevel(master)
    overdraftfees_screen.title('Overdraft Fees')
    #Label
    Label(overdraftfees_screen,text="Enter Overdraft Fee Amount to Charge: $",font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    #Entry
    Entry(overdraftfees_screen, textvariable=temp_odfee).grid(row=1,sticky=N,padx=5)
    #Button
    Button(overdraftfees_screen,text="Enter",command=overdraft_feeCharged,width=15,font=('Times New Roman',b)).grid(row=3,sticky=N,pady=5)
    
    cur.execute(f"SELECT ssn FROM customer WHERE balance < 0")
    conn.commit()
    neg_accounts = cur.fetchall()
    
def overdraft_feeCharged():
    global odfee
    global odfeestr
    odfee = float(temp_odfee.get())
    odfeestr = str(temp_odfee.get())
    od_feeCharged = Toplevel(master)
    od_feeCharged.title('Overdraft Fees')
    cur.execute(f"SELECT fees FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    f = cur.fetchone()
    fee = float(f[0])
    nfees = int(fee + odfee)
    cur.execute(f"UPDATE customer SET fees='{nfees}' WHERE SSN='{SSN}'")
    cur.execute(f"SELECT fees FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    cfees = cur.fetchone()
    cfeesstr = str(cfees[0])
    Label(od_feeCharged,text="The Following Overdraft Fee was Charged: $" + odfeestr,font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    Label(od_feeCharged,text="Current Total Fees: $" + cfeesstr,font=('Times New Roman',d)).grid(row=1,sticky=N,pady=10,padx=10)
    Button(od_feeCharged,text="Return to Account Management",command=account_management,width=30,font=('Times New Roman',b)).grid(row=2,sticky=N,pady=5)
    
def account_fees():
    global temp_fee
    temp_fee = StringVar()
    #Account Fees screen
    accountfees_screen = Toplevel(master)
    accountfees_screen.title('Account Fees')
    #Label
    Label(accountfees_screen,text="Enter Account Fee Amount to Charge: $",font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    #Entry
    Entry(accountfees_screen, textvariable=temp_fee).grid(row=1,sticky=N,padx=5)
    #Button
    Button(accountfees_screen,text="Enter",command=account_feeCharged,width=15,font=('Times New Roman',b)).grid(row=3,sticky=N,pady=5)
    
def account_feeCharged():
    global fee
    global feestr
    fee = float(temp_fee.get())
    feestr = str(temp_fee.get())
    acc_feeCharged = Toplevel(master)
    acc_feeCharged.title('Account Fees')
    cur.execute(f"SELECT fees FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    f = cur.fetchone()
    fe = float(f[0])
    nfees = int(fe + fee)
    cur.execute(f"UPDATE customer SET fees='{nfees}' WHERE SSN='{SSN}'")
    cur.execute(f"SELECT fees FROM customer WHERE SSN='{SSN}'")
    conn.commit()
    cfees = cur.fetchone()
    cfeesstr = str(cfees[0])
    Label(acc_feeCharged,text="The Following Account Fee was Charged: $" + feestr,font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    Label(acc_feeCharged,text="Current Total Fees: $" + cfeesstr,font=('Times New Roman',d)).grid(row=1,sticky=N,pady=10,padx=10)
    Button(acc_feeCharged,text="Return to Account Management",command=account_management,width=30,font=('Times New Roman',b)).grid(row=2,sticky=N,pady=5)

def personal_account_management():
    global temp_SSN
    global account_notif
    global personal_account_screen
    temp_SSN = StringVar()
    #Account Selection Screen
    personal_account_screen = Toplevel(master)
    personal_account_screen.title('Personal Account Management')
    #Labels
    Label(personal_account_screen, text="Enter Your SSN", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    #Entry
    Entry(personal_account_screen, textvariable=temp_SSN).grid(row=1,sticky=N,padx=5)
    #Button
    Button(personal_account_screen, text="Enter", command=personal_account, width=15,font=('Times New Roman',t)).grid(row=2,sticky=W,pady=5,padx=5)
    
def personal_account():
    #Vars
    ssnc = temp_SSN.get()
    cur.execute(f"SELECT ssn FROM customer WHERE ssn='{ssnc}'")
    conn.commit()
    login_screen.destroy()
    
    cur.execute(f"SELECT first_name FROM customer WHERE SSN='{ssnc}'")
    conn.commit()
    firstName = cur.fetchall()
    Fname = ''.join(firstName[0])
    
    cur.execute(f"SELECT last_name FROM customer WHERE SSN='{ssnc}'")
    conn.commit()
    lastName = cur.fetchall()
    Lname = ''.join(lastName[0])
    
    #monthly statement
    cur.execute(f"SELECT monthly_statement FROM customer WHERE SSN='{ssnc}'")
    conn.commit()
    ms = cur.fetchall()
    monthly_statement = ''.join(ms[0])
    
    #pending transactions
    cur.execute(f"SELECT pending_transaction FROM customer WHERE SSN='{ssnc}'")
    conn.commit()
    pt = cur.fetchall()
    pending_transactions = ''.join(pt[0])
    
    #balance
    cur.execute(f"SELECT balance FROM customer WHERE SSN='{ssnc}'")
    conn.commit()
    b = cur.fetchall()
    bal = b[0]
    bal2 = bal[0]
    balance = str(bal2)
    
    #Personal Account Management screen
    personal_account_management = Toplevel(master)
    personal_account_management.title('Personal Account Management')
    #Labels
    Label(personal_account_management, text="Personal Account Management", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
    Label(personal_account_management, text="Name: "+Fname + " " + Lname, font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(personal_account_management, text="Monthly Statement: "+monthly_statement, font=('Times New Roman',a)).grid(row=2,sticky=W)
    Label(personal_account_management, text="Pending Transactions: "+pending_transactions, font=('Times New Roman',a)).grid(row=4,sticky=W)
    Label(personal_account_management, text="Balance: $"+balance, font=('Times New Roman',a)).grid(row=5,sticky=W)
    #Buttons
    Button(personal_account_management, text="Create Account", font=('Times New Roman',b),width=30,command=create_account).grid(row=7,sticky=N,pady=10)
    Button(personal_account_management, text="Delete Account", font=('Times New Roman',b),width=30,command=delete_account).grid(row=8,sticky=N,pady=10) 

def create_account():
    #Vars
    global temp_account_SSN
    global temp_account_type
    global account_register_screen
    
    temp_account_SSN = StringVar()
    temp_account_type = StringVar()
    
    #Register Screen
    account_register_screen = Toplevel(master)
    account_register_screen.title('New Account')

    #Labels
    Label(account_register_screen, text="Please enter your details below to register:", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    Label(account_register_screen, text="SSN", font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(account_register_screen, text="Account Type (checking/saving)", font=('Times New Roman',a)).grid(row=2,sticky=W)
    notif = Label(account_register_screen, font=('Times New Roman',n))
    notif.grid(row=13,sticky=N,pady=10)

    #Entries
    Entry(account_register_screen,textvariable=temp_account_SSN).grid(row=1,column=1)
    Entry(account_register_screen,textvariable=temp_account_type).grid(row=2,column=1)
    
    #Buttons
    Button(account_register_screen, text="Create", command = finish_account_reg, font=('Times New Roman',b)).grid(row=14,sticky=N,pady=10)
    
def finish_account_reg():


    SSN_account_input = temp_account_SSN.get()
    account_type_input = temp_account_type.get()

    if SSN_account_input == "" or account_type_input == "" :
        login_notif = Label(account_register_screen, font=('Times New Roman',n))
        login_notif.grid(row=5,sticky=N)
        login_notif.config(fg="red",text="All fields required * ")
        return
    else:

        cur.execute(f"select branch_id from customer where ssn='{SSN_account_input}'")
        conn.commit()
        customer_branch_1 = cur.fetchall()
        customer_branch = customer_branch_1[0]
        branch = customer_branch[0]

 
        cur.execute(f"INSERT INTO  account3 VALUES(default,'{account_type_input}', 0, '{SSN_account_input}','{branch}')")
        conn.commit()
        
        cur.execute("SELECT account_num FROM account3 ORDER BY account_num DESC limit 1")
        conn.commit()
        current_account_num_1 = cur.fetchall()
        current_account_num_2 = current_account_num_1[0]
        current_account_num = str(current_account_num_2[0])
    
        login_notif = Label(account_register_screen, font=('Times New Roman',n))
        login_notif.grid(row=5,sticky=N)
        login_notif.config(fg="green",text="New account added! Account #:"+current_account_num)

    
def delete_account():
    #Vars
    global temp_account_SSN
    global account_delete_screen
    
    temp_account_SSN = StringVar()
    temp_account_type = StringVar()
    
    #Register Screen
    account_delete_screen = Toplevel(master)
    account_delete_screen.title('Select account to delete')

    #Labels
    Label(account_delete_screen, text="Please enter your details below to delete:", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    Label(account_delete_screen, text="SSN", font=('Times New Roman',a)).grid(row=1,sticky=W)
    notif = Label(account_delete_screen, font=('Times New Roman',n))
    notif.grid(row=13,sticky=N,pady=10)

    #Entries
    Entry(account_delete_screen,textvariable=temp_account_SSN).grid(row=1,column=1)
    
    #Buttons
    Button(account_delete_screen, text="Show accounts", command = show_account, font=('Times New Roman',b)).grid(row=14,sticky=N,pady=10)
    
def show_account():
    global temp_account_num
    global account_show_screen
    global row
    
    temp_account_num = StringVar()
    account_delete_screen.destroy()
    
    account_show_screen = Toplevel(master)
    account_show_screen.title('Select account to delete')
    
    account_SSN  = temp_account_SSN.get()
    
    cur.execute(f"SELECT * FROM account3 WHERE customerSSN='{account_SSN}'")
    conn.commit()
    account = cur.fetchall()
    
    Label(account_show_screen, text="Accounts", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
    
    row = 1
    if account != []:
        
        for i in range(len(account)):
            first_account = account[i]
            account_num = str(first_account[0])
            account_type = first_account[1]
            account_bal = str(first_account[2])

            #Labels
            Label(account_show_screen, text="Account Number: "+account_num, font=('Times New Roman',a)).grid(row=row,sticky=W)
            Label(account_show_screen, text="Account Type: "+account_type, font=('Times New Roman',a)).grid(row=row+1,sticky=W)
            Label(account_show_screen, text="Account Balance: "+account_bal, font=('Times New Roman',a)).grid(row=row+2,sticky=W)
            
            row = row+4

    else:
        login_notif = Label(customer_SSN_screen, font=('Times New Roman',n))
        login_notif.grid(row=5,sticky=N)
        login_notif.config(fg="red", text="enter valid SSN")
        
    Label(account_show_screen, text="Please enter the account you would like to delete:", font=('Times New Roman',d)).grid(row=row+1,sticky=N,pady=10)
    Entry(account_show_screen,textvariable=temp_account_num).grid(row=row+1,column=1)
    
    Button(account_show_screen, text="Delete", command = delete_account_cont, font=('Times New Roman',b)).grid(row=row+2,sticky=N,pady=10)

    
def delete_account_cont():
    
    delete_this_account = temp_account_num.get()

    cur.execute(f"DELETE FROM account3 WHERE account_num = '{delete_this_account}'")
    conn.commit()

    delete_notif = Label(account_show_screen, font=('Times New Roman',n))
    delete_notif.grid(row=row+3,sticky=N)
    delete_notif.config(fg="green",text="Account deleted!")
        
def toDeposit():
    global temp_account_num
    temp_account_num = StringVar()
    toDeposit_screen = Toplevel(master)
    toDeposit_screen.title('Confirmation Page')
    Label(toDeposit_screen,text="Please enter of account number: ",font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    Entry(toDeposit_screen,text=temp_account_num).grid(row=1,sticky=N,padx=5)
    Button(toDeposit_screen,text="Enter",command=deposit,width=15,font=('Times New Roman',b)).grid(row=3,sticky=N,pady=5)
    
def deposit():
    global temp_deposit
    temp_deposit = StringVar()
    #Deposit screen
    toDeposit_screen.destroy()
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
    Label(deposit_screen,text="Enter Amount to Deposit: $",font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    Entry(deposit_screen,text=temp_deposit).grid(row=1,sticky=N,padx=5)
    Button(deposit_screen,text="Enter",command=depositCalc,width=15,font=('Times New Roman',b)).grid(row=3,sticky=N,pady=5)
    
def depositCalc():
    global deposit
    global depositstr
    global SSN
    accountNum = temp_account_num.get()
    deposit = float(temp_deposit.get())
    depositstr = str(temp_deposit.get())
    depositCalc_screen = Toplevel(master)
    depositCalc_screen.title('Deposit')
    cur.execute(f"SELECT balance FROM account3 WHERE account_num='{accountNum}'")
    conn.commit()
    b = cur.fetchone()
    bal = float(b[0])
    nbalstr = str(b[0])
    nbal = float(bal + deposit)
    cur.execute(f"UPDATE account3 SET balance='{nbal}' where account_num='{accountNum}'")
    cur.execute(f"SELECT balance FROM account3 WHERE account_num='{accountNum}'")
    conn.commit()
    cbal = cur.fetchone()
    cbalstr = str(cbal[0])
    Label(depositCalc_screen,text="The Following Deposit was Made: $" + depositstr,font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    Label(depositCalc_screen,text="Balance Before Deposit: $" + nbalstr,font=('Times New Roman',d)).grid(row=1,stick=N)
    Label(depositCalc_screen,text="Current Balance: $" + cbalstr,font=('Times New Roman',d)).grid(row=2,sticky=N,pady=10,padx=10)
    #Button(depositCalc_screen,text="Return to Account Management",command=account_management,width=30,font=('Times New Roman',b)).grid(row=3,sticky=N,pady=5)

    
def withdraw():
    cur.execute(f"select * from account customerSSN = '{ssn_cust}';")
    user_Accounts = cur.fetchall()
    print("Accounts:\n")
    userAccountsDictionary ={}
    for i in range(len(user_Accounts)):
        userAccountsDictionary[int(i)] = user_Accounts[i][0]
        print(f"{i}: Id -> {user_Accounts[i][0]} Account Type -> {user_Accounts[i][1]} Balance-> {user_Accounts[i][2]} \n")
    account_ChoiceID = int(input("Please select account for withdrawal :"))
    withdrawal_amount = float(input("Please enter the amount you want to withdraw : "))
    cur.execute(f"select * from accounts where account_id = '{userAccountsDictionary[account_ChoiceID]}';")
    records = cur.fetchall()
    account_Balance = records[0][2] - amount
    if account_Balance < 0:
        print("Cannot perform this operation")
        print("Please try again with lesser amount")
    else:
        cursor.execute(f"update accounts set balance = {account_Balance} where account_id = '{userAccountsDictionary[account_ChoiceID]}';")
        print("Transaction Successful")
        print(f"Current Balance : {account_Balance}")
        cur.execute(f"insert into transaction values('Self', '{records[0][0]}', 'Withdrawal', {withdrawal_amount}, 'Credit Cash', current_timestamp);")    


def toTransfer():
    global temp_ownSSN
    temp_ownSSN = StringVar()
    toTransfer_screen = Toplevel(master)
    toTransfer_screen.title('Confirmation Page')
    Label(toTransfer_screen,text="Confirm Your SSN:",font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    Entry(toTransfer_screen,text=temp_ownSSN).grid(row=1,sticky=N,padx=5)
    Button(toTransfer_screen,text="Enter",command=transfer,width=15,font=('Times New Roman',b)).grid(row=3,sticky=N,pady=5)
def transfer():
    global temp_account_num_from
    global temp_account_num_to
    global temp_trans
    temp_trans = StringVar()
    temp_account_num_from = StringVar()
    temp_account_num_to = StringVar()
    transfer_screen = Toplevel(master)
    transfer_screen.title('Transfer Page')
    Label(transfer_screen,text="Enter account number to transfer money from",font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    Entry(transfer_screen,text=temp_account_num_from).grid(row=1,sticky=N,padx=5)
    Label(transfer_screen,text="Enter account number to transfer money to",font=('Times New Roman',d)).grid(row=2,sticky=N,pady=10,padx=10)
    Entry(transfer_screen,text=temp_account_num_to).grid(row=3,sticky=N,padx=5)
    Label(transfer_screen,text="Enter Transfer Amount",font=('Times New Roman',d)).grid(row=4,sticky=N,pady=10,padx=10)
    Entry(transfer_screen,text=temp_trans).grid(row=5,sticky=N,padx=5)
    Button(transfer_screen,text="Enter",command=transferCalc,width=15,font=('Times New Roman',b)).grid(row=6,sticky=N,pady=5)
    
def transferCalc():
    global trans
    global transstr

    accountNumfrom = temp_account_num_from.get()
    accountNumto = temp_account_num_to.get()

    

    trans = float(temp_trans.get())
    transstr = str(temp_trans.get())
    transferCalc_screen = Toplevel(master)
    transferCalc_screen.title('Transfer')
    
    cur.execute(f"SELECT balance FROM account3 WHERE account_num='{accountNumfrom}'")
    conn.commit()
    ownb = cur.fetchone()
    ownbal = float(ownb[0])
    ownbalstr = str(ownb[0])
    nownbal = float(ownbal - trans)
    cur.execute(f"UPDATE account3 SET balance='{nownbal}' WHERE account_num='{accountNumfrom}'")
    cur.execute(f"select balance from account3 WHERE account_num='{accountNumfrom}'")
    conn.commit()
    cownbal = cur.fetchone()
    cownbalstr = str(cownbal[0]) 
                
    cur.execute(f"SELECT balance FROM account3 WHERE account_num='{accountNumto}'")
    conn.commit()
    b = cur.fetchone()
    bal = float(b[0])
    balstr = str(b[0])
    nbal = float(bal + trans)
    cur.execute(f"UPDATE account3 SET balance='{nbal}' where account_num='{accountNumto}'")
    cur.execute(f"SELECT balance FROM account3 WHERE account_num='{accountNumto}'")
    conn.commit()
    cbal = cur.fetchone()
    cbalstr = str(cbal[0])
    
    Label(transferCalc_screen,text="The Following Amount was Transferred: $" + transstr,font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10,padx=10)
    Label(transferCalc_screen,text="Your Balance Before Transfer: $" + ownbalstr,font=('Times New Roman',d)).grid(row=1,sticky=N,pady=10,padx=10)            
    Label(transferCalc_screen,text="Your Balance After Transfer: $" + cownbalstr,font=('Times New Roman',d)).grid(row=2,sticky=N,pady=10,padx=10)
    Label(transferCalc_screen,text="Recipient's Balance Before Transfer: $" + balstr,font=('Times New Roman',d)).grid(row=3,sticky=N,pady=10,padx=10)
    Label(transferCalc_screen,text="Recipient's Balance After Transfer: $" + cbalstr,font=('Times New Roman',d)).grid(row=4,sticky=N,pady=10,padx=10)
    
    #Button(transferCalc_screen,text="Return to Account Management",command=account_management,width=30,font=('Times New Roman',b)).grid(row=5,sticky=N,pady=5)

def external_transfer():
    print("external transfer")
    
def personal_details():
    #Vars
    global temp_customer_SSN
    global customer_SSN_screen
    temp_customer_SSN = IntVar()
    #Personal details screen
    customer_SSN_screen = Toplevel(master)
    customer_SSN_screen.title('Please enter the SSN to view personal details')
    #Entry
    Entry(customer_SSN_screen, textvariable=temp_customer_SSN).grid(row=1,column=1,padx=5)
    #Button
    Button(customer_SSN_screen, text="Customer SSN", font=('Times New Roman',b),width=30,command=personal_details_view).grid(row=2,sticky=N,padx=10)

        
def personal_details_view():
    customer_SSN = temp_customer_SSN.get()
    
    cur.execute(f"SELECT * FROM customer WHERE SSN='{customer_SSN}'")
    conn.commit()
    customer_info_t = cur.fetchall()
    
    
    if customer_info_t != []:
        customer_info = customer_info_t[0]
        customer_fname = customer_info[1]
        customer_lname = customer_info[2]
        streetNum = str(customer_info[3])
        streetName = customer_info[4]
        aptNum = str(customer_info[5])
        city = customer_info[6]
        state = customer_info[7]
        zipp = str(customer_info[8])
        branch = str(customer_info[9])
        
        customer_SSN_screen.destroy()
        personal_details_screen = Toplevel(master)
        personal_details_screen.title('Customer Personal Details')
        
        #Labels
        Label(personal_details_screen, text="Personal Details", font=('Times New Roman',t)).grid(row=0,sticky=N,pady=10)
        Label(personal_details_screen, text="First Name: "+customer_fname, font=('Times New Roman',a)).grid(row=1,sticky=W)
        Label(personal_details_screen, text="Last Name: "+customer_lname, font=('Times New Roman',a)).grid(row=2,sticky=W)
        Label(personal_details_screen, text="Street Number: "+streetNum, font=('Times New Roman',a)).grid(row=3,sticky=W)
        Label(personal_details_screen, text="Street Name: "+streetName, font=('Times New Roman',a)).grid(row=4,sticky=W)
        Label(personal_details_screen, text="Apt Number: "+aptNum, font=('Times New Roman',a)).grid(row=5,sticky=W)
        Label(personal_details_screen, text="City: "+city, font=('Times New Roman',a)).grid(row=6,sticky=W)
        Label(personal_details_screen, text="State: "+state, font=('Times New Roman',a)).grid(row=7,sticky=W)
        Label(personal_details_screen, text="Zip Code: "+zipp, font=('Times New Roman',a)).grid(row=8,sticky=W)
        Label(personal_details_screen, text="Home branch: "+branch, font=('Times New Roman',a)).grid(row=9,sticky=W)
        return

    else:
        login_notif = Label(customer_SSN_screen, font=('Times New Roman',n))
        login_notif.grid(row=5,sticky=N)
        login_notif.config(fg="red", text=customer_SSN)

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
    global temp_login_SSN
    global login_notif
    global login_screen
    temp_login_SSN = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Manager Login')
    #Labels
    Label(login_screen, text="Login to your account", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="SSN", font=('Times New Roman',a)).grid(row=1,sticky=W)
    login_notif = Label(login_screen, font=('Times New Roman',n))
    login_notif.grid(row=5,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_SSN,show="*").grid(row=1,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=manager_session, width=15,font=('Times New Roman',t)).grid(row=4,sticky=W,pady=5,padx=5)
def loan_manager_login():
    #Vars
    global temp_login_SSN
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
    global temp_login_SSN
    global login_notif
    global login_screen
    temp_login_SSN = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Teller Login')
    #Labels
    Label(login_screen, text="Login to your account", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="SSN", font=('Times New Roman',a)).grid(row=1,sticky=W)
    login_notif = Label(login_screen, font=('Times New Roman',n))
    login_notif.grid(row=5,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_SSN,show="*").grid(row=1,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=teller_session, width=15,font=('Times New Roman',t)).grid(row=4,sticky=W,pady=5,padx=5)

def customer_login():
    #Vars
    global temp_login_Fname
    global temp_login_Lname
    global temp_login_SSN
    
    global login_notif
    global login_screen
    temp_login_Fname = StringVar()
    temp_login_Lname = StringVar()
    temp_login_SSN = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Customer Login')
    #Labels
    Label(login_screen, text="Login to your account", font=('Times New Roman',d)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="First Name", font=('Times New Roman',a)).grid(row=1,sticky=W)
    Label(login_screen, text="Last Name", font=('Times New Roman',a)).grid(row=2,sticky=W)
    Label(login_screen, text="SSN", font=('Times New Roman',a)).grid(row=3,sticky=W)
    login_notif = Label(login_screen, font=('Times New Roman',n))
    login_notif.grid(row=5,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_Fname).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_Lname).grid(row=2,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_SSN,show="*").grid(row=3,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=customer_session, width=15,font=('Times New Roman',t)).grid(row=4,sticky=W,pady=5,padx=5)

#Labels
Label(master, text = "Custom Banking Beta GUI", font=('Times New Roman', 30)).grid(row=0,sticky=N,pady=5,padx=30)
Label(master, text = "made by Group 1: Akina C., Ana S., Julia I.", font=('Times New Roman', d)).grid(row=1,sticky=N,pady=5)

#Buttons
Button(master, text="New Customer", font=('Times New Roman', b),width=20,command=register).grid(row=3,sticky=N)
Button(master, text="Login", font=('Times New Roman', b),width=20,command=role).grid(row=4,sticky=N,pady=10)

master.mainloop()

