import random
from config import CHAR_SETS

def generate_password(length):
    characters = CHAR_SETS["letters"] + CHAR_SETS["digits"] + CHAR_SETS["symbols"]
    return "".join(random.choice(characters) for _ in range(length))