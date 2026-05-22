import hashlib

username = input("Enter username: ")
password = input("Enter password: ")

# Hash entered password
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Store hashed password
stored_password = hashlib.sha256("StrongPassword123".encode()).hexdigest()

if username == "admin" and hashed_password == stored_password:
    print("Login Successful")
else:
    print("Invalid Login")    