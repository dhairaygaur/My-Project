from validator import validate_length
from generator import generate_password
from display import display_password
from strength_checker import password_strength
from history import save_password
from logger import log_event

def main():
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        return

    if not validate_length(length):
        print("Length must be between 6 and 32.")
        return

    password = generate_password(length)
    display_password(password)

    strength = password_strength(password)
    print("\nPassword Strength:", strength)

    save_password(password)
    log_event(f"Generated password of length {length} | Strength: {strength}")

if __name__ == "__main__":
    main()