#All Packages to make app work properly
import customtkinter
import hashlib
import tkinter
from tkinter import messagebox
from tkinter import PhotoImage
import sqlite3
#list of mail domains that will be accepted, You can add or remove mail domains or remove this feature at all.
#To disable this feature you can delete code from lines 92 to 95.
mail_domains = ['@gmail.com','@outlook.com','@hotmail.com','@proton.me','@yahoo.com']
#Function for signing In as an user. You can run your application from here adding your files and running main function of your app.
def SignIn():
    uname = username.get()
    passw = password.get()
    hashedpasswd = hashlib.sha256(passw.encode('utf-8')).hexdigest()
    if uname != '' and passw != '':
        db = sqlite3.connect("database/accounts.db")
        curr = db.cursor()
        curr.execute('SELECT password from users WHERE userID=?',[uname])
        result = curr.fetchone()
        if result:
            if hashedpasswd == result[0]:
                messagebox.showinfo(title="Success!",message="Successfully loged in As : " + uname)
            else:
                messagebox.showerror(title="Error",message="Invalid Password!")
    else:
        messagebox.showerror(title="Error",message="Please enter all data!")
#Function for switching to dark color mode 🌕.
def switch_to_darkmode():
    print("Switched to Dark Color mode!")
    root.configure(fg_color="#1c1c1c")
    loginimg.configure(image=darkmode)
    password.configure(fg_color="#1c1c1c",bg_color="#1c1c1c",text_color="#4287f5")
    selectcolor.configure(fg_color="#1c1c1c",hover_color="#1c1c1c",image=sun,command=switch_to_lightmode)
    showbtn.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
    username.configure(fg_color="#1c1c1c",text_color="#4287f5")
    button2.configure(fg_color="#1c1c1c",hover_color="#1c1c1c")
    email.configure(border_width=1,fg_color="#1c1c1c",placeholder_text="Email",text_color="#4287f5",placeholder_text_color="#4287f5")
#Function for switching to light color mode☀️(App default).
def switch_to_lightmode():
    print("Switched to Light Color mode!")
    root.configure(fg_color="#fff")
    selectcolor.configure(fg_color="#fff",hover_color="#fff",command=switch_to_darkmode,image=moon)
    loginimg.configure(image=lightmode)
    email.configure(fg_color="#fff")
    username.configure(fg_color="#fff")
    password.configure(fg_color="#fff")
    button2.configure(fg_color="#fff",hover_color="#fff")
    showbtn.configure(fg_color="#fff",hover_color="#fff")
#Function to make Password visible.
def ShowPassword():
    print("Password was set to visible")
    password.configure(show="")
    showbtn.configure(command=HidePassword)
    showbtn.configure(image=closedeye)
#Function to make password hideen.
def HidePassword():
    print("Password was set to not visible")
    password.configure(show="*")
    showbtn.configure(command=ShowPassword)
    showbtn.configure(image=eye)
#Function to toogle Login mode.
def switch_to_login():
    print("Switched to Login Mode")
    label1.configure(text="Sign In")
    label.configure(text="Not an User?")
    label.place(x=680,y=266)
    button2.configure(command=switch_to_register,text="Sign Up")
    button2.place(y=266)
    button.configure(text="Sign In",command=SignIn)
    button.place(x=630,y=225)
    email.place(x=610,y=900)
#Function to Switch back to Register mode.
def switch_to_register():
    print("Switched to Register Mode")
    label1.configure(text="Sign Up")
    label.configure(text="Already an User?")
    label.place(x=650, y=326)
    button2.configure(command=switch_to_login, text="Sign In")
    button.configure(command=SignUP,text="Sign Up")
    button.place(x=630,y=288)
    button2.place(x=780,y=328)
    email.configure(state='normal',border_width=1,border_color="#4287f5",text_color="#4287f5",placeholder_text_color="#4287f5",placeholder_text="Email")
    email.place(x=610, y=228)
#Function for creating new user.
def SignUP():
    
    userID = username.get()
    pswd = password.get()
    eml = email.get()
    contain_domain = any(domain in eml for domain in mail_domains)
    if not contain_domain:
        messagebox.showerror(title="Error!",message="Please provide Valid Mail")
        return
    else:
        db = sqlite3.connect("database/accounts.db")
        curr = db.cursor()
        if userID != '' and pswd != '' and eml != '':
            curr.execute("SELECT userID from users WHERE userID=?", [userID])
            curr.execute("SELECT email from users WHERE email=?", [eml])
            if curr.fetchone() is not None:
                tkinter.messagebox.showerror(message="User Already exists Sign In or Pick other Username.")
            else:
                hashedpassword = hashlib.sha256(pswd.encode('utf-8')).hexdigest()
                curr.execute("INSERT INTO users VALUES(?,?,?)",[userID,hashedpassword,eml])
                db.commit()
                db.close()
                tkinter.messagebox.showinfo(title="Success!",message="Successfully created account.")
        else:
            tkinter.messagebox.showerror(title="Error!",message="Error, Enter all data.")

#Code of main App.
def App():

    global username
    global password
    global showbtn
    global closedeye
    global eye
    global label1
    global label
    global button2
    global button
    global email
    global sun
    global moon
    global lightmode
    global darkmode
    global root
    global loginimg
    global selectcolor

    root = customtkinter.CTk(fg_color="#fff") #Making window background White
    root.geometry("960x550") #Making window 950px width and 550px height
    root.resizable(False,False) #Makes window not resizable
    root.title('Login Here') #Title Of the window
    root.iconbitmap("assets/icon.ico") #Path to Icon of the Window
    lightmode = PhotoImage(file="assets/loginlight.png") #Image of Light Version of the main image
    sun = PhotoImage(file="assets/sun.png") #Image for color theme button
    moon = PhotoImage(file="assets/moon.png") #Image for color theme button
    darkmode = PhotoImage(file="assets/logindark.png") #Image of Dark version of the main image
    eye = PhotoImage(file="assets/eyesmall.png") #Image of open eye for password visibility
    closedeye = PhotoImage(file="assets/closed.png") #Image of closed eye for password visibility

    loginimg = customtkinter.CTkLabel(root,image=lightmode,fg_color="#fff",text="") #Image in App
    loginimg.place(x=50,y=90)

    label1 = customtkinter.CTkLabel(root,text="Sign UP",font=('Microsoft Yahei UI Light',23),text_color="#4287f5") #Label above all entry boxes
    label1.place(x=700,y=56)

    username = customtkinter.CTkEntry(root,width=265,height=45,corner_radius=6,border_width=1,border_color="#4287f5",placeholder_text="Username",placeholder_text_color="#4287f5",font=('Microsoft Yahei UI Light',13),fg_color="#fff",bg_color="#fff",text_color="#000000") #Entry Box for Taking username.
    username.place(x=610,y=110)

    password = customtkinter.CTkEntry(root,width=265,height=45,corner_radius=6,border_width=1,border_color="#4287f5",placeholder_text="Password",placeholder_text_color="#4287f5",font=('Microsoft Yahei UI Light',13),fg_color="#fff",bg_color="#fff",text_color="#000000",show="*") #Entry Box for Taking Password.
    password.place(x=610,y=168)

    showbtn = customtkinter.CTkButton(root,image=eye,width=25,height=25,text="",fg_color="#fff",hover_color="#fff",command=ShowPassword) #Button for toogling on/off password visibility
    showbtn.place(x=880,y=175)

    email = customtkinter.CTkEntry(root,width=265,height=45,corner_radius=6,border_width=1,border_color="#4287f5",placeholder_text="Email",placeholder_text_color="#4287f5",font=('Microsoft Yahei UI Light',13),fg_color="#fff",bg_color="#fff",text_color="#000000") #code for taking user email as input.
    email.place(x=610,y=228)

    button = customtkinter.CTkButton(root,width=225,height=35,corner_radius=5,text="Sign Up",fg_color="#4287f5",command=SignUP) #Button for commiting Register / Login Function
    button.place(x=630,y=288)

    label = customtkinter.CTkLabel(root,text="Already an user?",font=('Microsoft Yahei UI Light',13),text_color="#4287f5") #Label taking user to Login Form if already an user
    label.place(x=650,y=326)

    button2 = customtkinter.CTkButton(root,text="Sign In",font=('Microsoft Yahei UI Light',12),text_color="#4287f5",fg_color="#fff",width=30,height=20,hover_color="#fff",command=switch_to_login) #Button to switch to the Login Form.
    button2.place(x=780,y=328)

    selectcolor = customtkinter.CTkButton(root,image=moon,width=5,height=20,text="",fg_color="#fff",hover_color="#fff",command=switch_to_darkmode) #Button for changing color theme.
    selectcolor.place(x=900,y=25)
    root.mainloop()
App()
