from validator import validate_length
from generator import generate_password

def run_tests():
    print("TESTING MODULES...\n")

    # Test 1 – length validator
    print("Length 5 valid?", validate_length(5))   # Expect False
    print("Length 10 valid?", validate_length(10)) # Expect True

    # Test 2 – password generator
    pwd = generate_password(8)
    print("Generated password:", pwd)
    print("Length correct?", len(pwd) == 8)

if __name__ == "__main__":
    run_tests()