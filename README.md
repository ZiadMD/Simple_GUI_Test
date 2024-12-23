# SecureLogin

This is a simple and secure login system implemented using Python's Tkinter library. The program provides a graphical user interface (GUI) that allows users to sign in and sign up. Passwords are securely hashed before being stored in a JSON file.
## Features

- **Sign Up**: Allows new users to register with a username and password.
- **Sign In**: Allows existing users to log in by verifying their credentials.
- **Password Hashing**: Passwords are securely stored using SHA-256 hashing.
- **Error Handling**: Provides feedback for invalid inputs (e.g., empty fields, incorrect credentials).

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3.x
- Tkinter (comes pre-installed with Python)
- `hashlib` and `json` libraries (both are part of Python’s standard library)

## Installation

1. Clone the repository or download the script files.

2. Install the required dependencies using the following command (if not already installed):
   ```shell
   pip install tk
   ```

## Usage

1. To run the code, execute the following command:
   ```shell
   python login.py
   ```

2. The login system GUI will appear. You can either:

   - **Sign In**: Enter your existing username and password to log in.
   - **Sign Up**: Create a new account by entering a username and password.

   Passwords are securely hashed before being saved to the `users.json` file.


