from tkinter import *
from tkinter import messagebox
import json


def signup():
    username = user_signup.get()
    passwd = pwd_signup.get()
    passwdconfo = conform_code.get()
    if passwd == passwdconfo:
        try:
            with open(r'users.json', 'r') as file:
                d = json.load(file)
            d[username] = passwd

            with open('users.json', 'w') as file:
                json.dump(d, file)

            messagebox.showinfo('Signup', 'Signup completed')

        except Exception as e:
            messagebox.showerror('Error', str(e))
    else:
        messagebox.showerror('Invalid', 'Passwords don\'t match')


def on_enter_pwd_signup(e):
    pwd_signup.delete(0, 'end')
    pwd_signup.config(show='*')


def on_leave_pwd_signup(e):
    passwd = pwd_signup.get()
    if passwd == '':
        pwd_signup.insert(0, 'Password')
        pwd_signup.config(show='')


def on_enter_conform_signup(e):
    conform_code.delete(0, 'end')
    conform_code.config(show='*')


def on_leave_conform_signup(e):
    passwd = conform_code.get()
    if passwd == '':
        conform_code.insert(0, 'Conform Password')
        conform_code.config(show='')


def on_enter_usr_signup(e):
    user_signup.delete(0, 'end')


def on_leave_usr_signup(e):
    name = user_signup.get()
    if name == '':
        user_signup.insert(0, 'Username')


def sign():
    window.destroy()


window = Tk()
window.title('SignUp')
window.geometry('925x500+300+200')
window.config(bg="#fff")
window.resizable(False, False)

img_signup = PhotoImage(file='login.png')
Label(window, image=img_signup, bg='white').place(x=50, y=90)

frame_signup = Frame(window, width=350, height=390, bg='white')
frame_signup.place(x=480, y=70)

heading_signup = Label(frame_signup, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading_signup.place(x=100, y=5)

# ------------------------------------------------------------------------------------------------ #
# user field

user_signup = Entry(frame_signup, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user_signup.place(x=30, y=80)
user_signup.insert(0, 'Username')
user_signup.bind('<FocusIn>', on_enter_usr_signup)
user_signup.bind('<FocusOut>', on_leave_usr_signup)

Frame(frame_signup, width=295, height=2, bg='black').place(x=25, y=107)
# ------------------------------------------------------------------------------------------------ #
# password field

pwd_signup = Entry(frame_signup, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11), show='*')
pwd_signup.place(x=30, y=150)
pwd_signup.insert(0, 'Password')
pwd_signup.config(show='')
pwd_signup.bind('<FocusIn>', on_enter_pwd_signup)
pwd_signup.bind('<FocusOut>', on_leave_pwd_signup)

Frame(frame_signup, width=295, height=2, bg='black').place(x=25, y=177)
# ------------------------------------------------------------------------------------------------ #
# conform password field

conform_code = Entry(frame_signup, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
conform_code.place(x=30, y=220)
conform_code.insert(0, 'Conform Password')
conform_code.config(show='')
conform_code.bind('<FocusIn>', on_enter_conform_signup)
conform_code.bind('<FocusOut>', on_leave_conform_signup)

Frame(frame_signup, width=295, height=2, bg='black').place(x=25, y=247)
# ------------------------------------------------------------------------------------------------ #
# Buttons field
Button(frame_signup, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
label_signup = Label(frame_signup, text='I have an account', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label_signup.place(x=90, y=340)

sign_in = Button(frame_signup, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
sign_in.place(x=200, y=340)


window.mainloop()
