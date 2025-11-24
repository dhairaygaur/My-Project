def save_password(password):
    with open("password_history.txt", "a") as f:
        f.write(password + "\n")