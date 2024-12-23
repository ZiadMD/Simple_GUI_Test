import json
import hashlib
from tkinter import *
from tkinter import messagebox


# -------------------- Utility Functions -------------------- #

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def load_users(file_path='users.json'):
    """Loads user data from the JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_users(users, file_path='users.json'):
    """Saves user data to the JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(users, file)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save users: {str(e)}")


def validate_input(username, password):
    """Validates that the username and password are not empty."""
    if not username or not password:
        messagebox.showerror("Invalid Input", "Username and password cannot be empty.")
        return False
    return True


# -------------------- Authentication Functions -------------------- #

def signin():
    """Handles user login."""
    users = load_users()
    username = user.get()
    password = pwd.get()

    if not validate_input(username, password):
        return

    hashed_password = users.get(username)
    if hashed_password and hashed_password == hash_password(password):
        show_profile(username)
    else:
        messagebox.showerror("Invalid", "Invalid username or password")


def signup():
    """Handles user registration."""
    username = user_signup.get()
    password = pwd_signup.get()
    confirm_password = confirm_code.get()

    if not validate_input(username, password):
        return

    if password != confirm_password:
        messagebox.showerror("Invalid", "Passwords don't match")
        return

    users = load_users()
    if username in users:
        messagebox.showerror("Invalid", "Username already exists")
        return

    users[username] = hash_password(password)
    save_users(users)
    messagebox.showinfo("Signup", "Signup completed")
    signup_window.destroy()


# -------------------- UI Functions -------------------- #

def show_profile(username):
    """Displays the profile screen after successful login."""
    screen = Toplevel(root)
    screen.title("Profile")
    screen.geometry("925x500+300+200")
    screen.config(bg="white")
    Label(screen, text=f"Hello {username}", bg="#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)


def open_signup_window():
    """Opens the signup window."""
    global signup_window, user_signup, pwd_signup, confirm_code

    signup_window = Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("925x500+300+200")
    signup_window.config(bg="#fff")
    signup_window.resizable(False, False)

    img_signup = PhotoImage(file='login.png')
    Label(signup_window, image=img_signup, bg='white').place(x=50, y=90)
    signup_window.img_signup = img_signup

    # UI Components for Signup
    frame_signup = Frame(signup_window, width=350, height=390, bg="white")
    frame_signup.place(x=480, y=70)

    Label(frame_signup, text="Sign Up", fg="#57a1f8", bg="white",
          font=("Microsoft Yahei UI Light", 23, "bold")).place(x=100, y=5)

    # Username
    user_signup = create_entry(frame_signup, "Username", 80)

    # Password
    pwd_signup = create_entry(frame_signup, "Password", 150, is_password=True)

    # Confirm Password
    confirm_code = create_entry(frame_signup, "Confirm Password", 220, is_password=True)

    # Buttons
    Button(frame_signup, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white",
           border=0, command=signup).place(x=35, y=280)
    Label(frame_signup, text="I have an account", fg="black", bg="white",
          font=("Microsoft Yahei UI Light", 9)).place(x=90, y=340)
    Button(frame_signup, width=6, text="Sign In", border=0, bg="white", cursor="hand2", fg="#57a1f8",
           command=signup_window.destroy).place(x=200, y=340)


def create_entry(frame, placeholder, y_position, is_password=False):
    """Creates an Entry widget with placeholder text."""
    entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    entry.place(x=30, y=y_position)
    entry.insert(0, placeholder)

    if is_password:
        entry.bind("<FocusIn>", lambda e: (entry.delete(0, "end"), entry.config(show="*")))
        entry.bind("<FocusOut>", lambda e: entry.insert(0, placeholder) if entry.get() == "" else None)
    else:
        entry.bind("<FocusIn>", lambda e: entry.delete(0, "end"))
        entry.bind("<FocusOut>", lambda e: entry.insert(0, placeholder) if entry.get() == "" else None)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=y_position + 27)
    return entry


# -------------------- Main Application -------------------- #

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(False, False)

# Login UI
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

try:
    img_login = PhotoImage(file='pylog2.png')
    Label(root, image=img_login, bg='white').place(x=50, y=50)
except TclError:
    Label(root, text="Login App", font=("Arial", 20), bg='white').place(x=50, y=50)

Label(frame, text="Sign in", fg="#57a1f8", bg="white",
      font=("Microsoft Yahei UI Light", 23, "bold")).place(x=100, y=5)

# Username
user = create_entry(frame, "Username", 80)

# Password
pwd = create_entry(frame, "Password", 150, is_password=True)

# Buttons
Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg="white",
       border=0, command=signin).place(x=35, y=204)
Label(frame, text="Don't have an account?", fg="black", bg="white",
      font=("Microsoft Yahei UI Light", 9)).place(x=32, y=250)
Button(frame, width=6, text="Sign Up", border=0, bg="white", cursor="hand2", fg="#57a1f8",
       command=open_signup_window).place(x=260, y=253)

root.mainloop()
