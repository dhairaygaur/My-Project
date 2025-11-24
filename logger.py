def log_event(message):
    with open("activity.log", "a") as f:
        f.write(message + "\n")