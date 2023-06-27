# Code Login System

This is a simple login system implemented using Python's Tkinter library. The program allows users to sign in and sign up using a graphical user interface (GUI).

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3
- Tkinter library

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies using the following command:

pip install tkinter


## Usage

To run the code, execute the following command: python login.py


The login system GUI will appear, allowing you to sign in or sign up.

## Features

### Sign In

- Enter your username and password in the respective fields.
- Click the "Sign in" button to log in.
- If the entered username and password match an existing user in the `users.json` file, a new window will open displaying a welcome message with the username.
- If the username or password is invalid, an error message will be displayed.

### Sign Up

- Click the "Sign UP" button on the login page to open the sign-up window.
- Enter a username, password, and confirm the password.
- Click the "Sign Up" button to create a new user.
- If the passwords match, the new user will be added to the `users.json` file, and a success message will be displayed.
- If the passwords do not match, an error message will be displayed.


