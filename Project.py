from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

def connect():
    try:
        conn = mysql.connector.connect(host='localhost', database='project', user='root', password='')
        if conn.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(e)
if __name__ == '__main__':
    connect()
    
conn = mysql.connector.connect(host='localhost', database='project', user='root', password='')
cursor = conn.cursor()    

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
   
window = Tk()
window.title("IBS : SIGNUP")
window.geometry("600x400")
center(window)
lhead = Label(window, width="600", text="Banking System", fg="white", bg="lightblue", compound=CENTER, font=("fixedsys", 20, "bold"))
lhead.pack(side="top", padx=10, pady=10)
lsignup = Label(window, width="600", text="If New User, fill details & press Submit", fg="white", bg="#52BE80", compound=CENTER, font=("system", 15, "bold"))
lsignup.pack(padx=10, pady=(0,10))
master = Frame(window)
master.pack()
bt1 = Button(window, text="Submit", fg="white", bg="lightblue", width="10", command = lambda : submitsignup())
bt1.place(x=200, y=303)
bt2 = Button(window, text="Login", width="10", fg="white", bg="#52BE80", command = lambda : login())
bt2.place(x=325, y=303)
l1 = Label(master, text = "Full name :", padx=5, pady=5).grid(row=0)
l2 = Label(master, text = "Username :", padx=5, pady=5).grid(row=1)
l3 = Label(master, text = "Password :", padx=5, pady=5).grid(row=2)
l4 = Label(master, text = "Email-ID :", padx=5, pady=5).grid(row=3)
l5 = Label(master, text = "Contact No. :", padx=5, pady=5).grid(row=4)
l6 = Label(master, text = "Account No. :", padx=5, pady=5).grid(row=5)
l7 = Label(master, text = "IFSC Code :", padx=5, pady=5).grid(row=6)
FULLNAME = Entry(master)
FULLNAME.grid(row=0, column=1)
USERNAME = Entry(master)
USERNAME.grid(row=1, column=1)
PASSWORD = Entry(master, show="*")
PASSWORD.grid(row=2, column=1)
EMAIL = Entry(master)
EMAIL.grid(row=3, column=1)
CONTACT = Entry(master)
CONTACT.grid(row=4, column=1)
ACCNO = Entry(master)
ACCNO.grid(row=5, column=1)
IFSC = Entry(master)
IFSC.grid(row=6, column=1)

def submitsignup():    
    a = FULLNAME.get()
    b = USERNAME.get()
    c = PASSWORD.get()
    d = EMAIL.get()
    e = CONTACT.get()
    f = ACCNO.get()
    g = IFSC.get()

    ser = ("SELECT USERNAME FROM SIGNUP WHERE USERNAME ='%s'" % (b))
    cursor.execute(ser)
    userrow = cursor.fetchall()
    ser1 = ("SELECT USERNAME FROM SIGNUP WHERE ACCNO ='%s'" % (f))
    cursor.execute(ser1)
    accrow = cursor.fetchall()
    if userrow:
        messagebox.showerror("Error","Username taken!")
    elif accrow:
        messagebox.showerror("Error","Account number already Registered.")
    else :
        ins = ("INSERT INTO SIGNUP(FULLNAME, USERNAME, PASSWORD, EMAIL, CONTACT, ACCNO, IFSC) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (a, b, c, d, e, f, g))
        cursor.execute(ins)    

def login():
    window.destroy()
    #global lwindow
    lwindow = Tk()
    lwindow.title("IBS : LOGIN")
    lwindow.geometry("600x400")
    center(lwindow)
    loghead = Label(lwindow, width="600", text="Login", fg="white", bg="lightblue", compound=CENTER, font=("fixedsys", 20, "bold"))
    loghead.pack(side="top", padx=10, pady=10)
    log = Label(lwindow, width="600", text="Enter Login Details", fg="white", bg="#52BE80", compound=CENTER, font=("system", 15, "bold"))
    log.pack(padx=10, pady=(0,10))
    lmaster = Frame(lwindow)
    lmaster.pack()
    log = Button(lwindow, text="Login", width="10", fg="white", bg="lightblue", command = lambda : submitlogin())
    log.place(x=205, y=153)
    log1 = Label(lmaster, text = "Username :", padx=5, pady=5).grid(row=0)
    log2 = Label(lmaster, text = "Password :", padx=5, pady=5).grid(row=1)
    login.USERNAME = Entry(lmaster)
    login.USERNAME.grid(row=0, column=1)
    login.PASSWORD = Entry(lmaster,show="*")
    login.PASSWORD.grid(row=1, column=1)
    
def submitlogin():
    global h
    global i
    h = login.USERNAME.get()
    i = login.PASSWORD.get()
    cursor.execute("SELECT * FROM SIGNUP WHERE USERNAME = '%s' AND PASSWORD = '%s'" % (h,i))
    result = cursor.fetchone()
    
    if result is None:
        messagebox.showerror("Error","Invalid Username OR Password")
    else:
        messagebox.showinfo("Done","Sucessfully Logged In.")
        
#----------Now writing code for window which will popup after sucessfull login----------#

        mwindow = Tk()
        mwindow.title("IBS : USER INFORMATION")
        mwindow.geometry("600x400")
        center(mwindow)
        dhead = Label(mwindow, width="600", text="Menu", fg="white", bg="lightblue", compound=CENTER, font=("fixedsys", 20, "bold"))
        dhead.pack(side="top", padx=10, pady=10)
        dh = Label(mwindow, width="600", text="Select an Option", fg="white", bg="#52BE80", compound=CENTER, font=("system", 15, "bold"))
        dh.pack(padx=10, pady=(0,10))
        mmaster = Frame(mwindow)
        mmaster.pack()
        vud = Button(mwindow, text="USER DETAILS", fg="white", bg="#5DADE2", width="20", command = lambda : userdetail())
        vud.place(x=135, y=115)
        cb = Button(mwindow, text="CHECK BALANCE", fg="white", bg="#5DADE2", width="20", command = lambda : checkbalance())
        cb.place(x=345, y=115)
        dm = Button(mwindow, text="DEPOSIT", fg="white", bg="#5DADE2", width="20", command = lambda : deposit())
        dm.place(x=135, y=165)
        wm = Button(mwindow, text="WITHDRAW", fg="white",bg="#5DADE2", width="20", command = lambda : withdraw())
        wm.place(x=345, y=165)
        tm = Button(mwindow, text="TRANSFER", fg="white",bg="#5DADE2", width="20", command = lambda : transfer())
        tm.place(x=135, y=215)
        cu = Label(mwindow, width="600", text="Current User Logged in : "+login.USERNAME.get(), fg="white", bg="#F5B041", compound=CENTER, font=("system", 15, "bold"))
        cu.pack(padx=10, pady=(0,10), side="bottom")
        ud = Button(mwindow, text="LOGOUT", fg="white", bg="#58D68D", width="20", command = lambda : mwindow.destroy())
        ud.place(x=345, y=215)

def userdetail():
    global j
    j = h
    que1 = ("SELECT * FROM SIGNUP WHERE USERNAME = '%s'" % (j))
    cursor.execute(que1)
    dta = cursor.fetchone()
    ud = Tk()
    ud.title("DETAILS")
    ud.geometry("600x400")
    center(ud)
    udl = Label(ud, width="600", text="Your Registration Details Are : ", fg="white", bg="lightblue", compound=CENTER, font=("fixedsys", 20, "bold"))
    udl.pack(side="top", padx=10, pady=10)
    udmaster = Frame(ud)
    udmaster.pack()
    udl1 = Label(udmaster, text = "Full name :", padx=5, pady=5).grid(row=0)
    udl2 = Label(udmaster, text = "Username :", padx=5, pady=5).grid(row=1)
    udl3 = Label(udmaster, text = "Email-ID :", padx=5, pady=5).grid(row=2)
    udl4 = Label(udmaster, text = "Contact No. :", padx=5, pady=5).grid(row=3)
    udl5 = Label(udmaster, text = "Account No. :", padx=5, pady=5).grid(row=4)
    udl6 = Label(udmaster, text = "IFSC Code :", padx=5, pady=5).grid(row=5)
    det1 = Label(udmaster, text=dta[0], font=("arial", 14, "bold"))
    det1.grid(row=0, column=1)
    det2 = Label(udmaster, text=dta[1], font=("arial", 14, "bold"))
    det2.grid(row=1, column=1)
    det3 = Label(udmaster, text=dta[3], font=("arial", 14, "bold"))
    det3.grid(row=2, column=1)
    det4 = Label(udmaster, text=dta[4], font=("arial", 14, "bold"))
    det4.grid(row=3, column=1)
    det5 = Label(udmaster, text=dta[5], font=("arial", 14, "bold"))
    det5.grid(row=4, column=1)
    det6 = Label(udmaster, text=dta[6], font=("arial", 14, "bold"))
    det6.grid(row=5, column=1)
    udback = Button(ud, text = "Back", width="10", fg="white", bg="#52BE80", command = lambda : ud.destroy())
    udback.place(x=325 ,y=303)

def checkbalance():
    global k
    k = h
    que2 = ("SELECT BALANCE FROM SIGNUP WHERE USERNAME = '%s'" % (k))
    cursor.execute(que2)
    bala = cursor.fetchone()
    bal = Tk()
    bal.title("BALANCE")
    bal.geometry("600x400")
    center(bal)
    balmaster = Frame(bal)
    balmaster.pack()
    ball1 = Label(bal, text = "Your Account Balance is :", font = 14, padx=5, pady=5)
    ball1.place(x=190, y=190)
    ball2 = Label(bal, text = bala[0], font=("arial", 14, "bold"))
    ball2.place(x=390, y=190)
    ballback = Button(bal, text="Back", width="10", fg="white", bg="#52BE80", command = lambda : bal.destroy())
    ballback.place(x=325, y=303)
    
def deposit():
    global l
    l = h
    dep = Tk()
    dep.title("DEPOSIT MONEY")
    dep.geometry("600x400")
    center(dep)
    depl1 = Label(dep, text = "Enter the Amount you want to Deposit :", font = 14, padx=5, pady=5)
    depl1.place(x=100, y=140)
    deposit.depl2 = Entry(dep)
    deposit.depl2.place(x=390, y=145)
    subdep = Button(dep, text="Deposit", fg="white", bg="lightblue", width="10", command = lambda : submitdeposit())
    subdep.place(x=200, y=303)
    bdep = Button(dep, text="Back", width="10", fg="white", bg="#52BE80", command = lambda : dep.destroy())
    bdep.place(x=325, y=303)
    
def submitdeposit():
    
    val = float(deposit.depl2.get())
    que3 = ("SELECT BALANCE FROM SIGNUP WHERE USERNAME = '%s'" % h)
    cursor.execute(que3)
    bal = cursor.fetchone()
    fbal = bal[0]+val
    que2 = ("UPDATE SIGNUP SET BALANCE = %s WHERE USERNAME ='%s'" % (fbal, h))
    cursor.execute(que2)
    messagebox.showinfo("Done","Sucessfully Deposited.")
    

def withdraw():
    global m
    m = h
    wit = Tk()
    wit.title("WITHDRAW MONEY")
    wit.geometry("600x400")
    center(wit)
    witl1 = Label(wit, text = "Enter the Amount you want to Withdraw :", font = 14, padx=5, pady=5)
    witl1.place(x=100, y=140)
    withdraw.witl2 = Entry(wit)
    withdraw.witl2.place(x=390, y=145)
    subwit = Button(wit, text="Withdraw", fg="white", bg="lightblue", width="10", command = lambda : submitwithdraw())
    subwit.place(x=200, y=303)
    bwit = Button(wit, text="Back", width="10", fg="white", bg="#52BE80", command = lambda : wit.destroy())
    bwit.place(x=325, y=303)


def submitwithdraw():

    wval = float(withdraw.witl2.get())
    que4 = ("SELECT BALANCE FROM SIGNUP WHERE USERNAME = '%s'" % h)
    cursor.execute(que4)
    wbal = cursor.fetchone()
    if wval > wbal[0]:
        messagebox.showerror("Error","Not Sufficient Balance. \n Balance is : " +str(wbal[0]))
    else:
        fwbal = wbal[0]-wval
        que5 = ("UPDATE SIGNUP SET BALANCE = %s WHERE USERNAME ='%s'" % (fwbal, h))
        cursor.execute(que5)
        messagebox.showinfo("Done","Sucessfully Withdrawn.")

def transfer():
    global n
    n = h
    tra = Tk()
    tra.title("TRANSFER MONEY")
    tra.geometry("600x400")
    center(tra)
    tral1 = Label(tra, text = "Enter the Amount you want to Transfer :", font = 14, padx=5, pady=5)
    tral1.place(x=100, y=140)
    tral2 = Label(tra, text = "Enter Username where to Transfer :", font = 14, padx=5, pady=5)
    tral2.place(x=100, y=190)
    transfer.tral3 = Entry(tra)
    transfer.tral3.place(x=390, y=145)
    transfer.tral4 = Entry(tra)
    transfer.tral4.place(x=390, y=195)
    subtra = Button(tra, text="Transfer", fg="white", bg="lightblue", width="10", command = lambda : submittransfer())
    subtra.place(x=200, y=303)
    btra = Button(tra, text="Back", width="10", fg="white", bg="#52BE80", command = lambda : tra.destroy())
    btra.place(x=325, y=303)

def submittransfer():

    tval = float(transfer.tral3.get())
    tname = transfer.tral4.get()
    que6 = ("SELECT BALANCE FROM SIGNUP WHERE USERNAME = '%s'" % h)
    cursor.execute(que6)
    tbal = cursor.fetchone()
    que100 = ("SELECT BALANCE FROM SIGNUP WHERE USERNAME = '%s'" % tname)
    cursor.execute(que100)
    tbal10 = cursor.fetchone()
    if tval > tbal[0]:
        messagebox.showerror("Error","Not Sufficient Balance. \n Balance is : " +str(tbal[0]))
    else:
        u1 = tbal[0]-tval
        u2 = tbal10[0]+tval
        que7 = ("UPDATE SIGNUP SET BALANCE = %s WHERE USERNAME ='%s'" % (u1, h))
        cursor.execute(que7)
        que8 = ("UPDATE SIGNUP SET BALANCE = %s WHERE USERNAME ='%s'" % (u2, tname))
        cursor.execute(que8)
        messagebox.showinfo("Done","Sucessfully Transferred.")
        
