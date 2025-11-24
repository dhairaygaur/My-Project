def password_strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(not c.isalnum() for c in password): score += 1

    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score >= 3:
        return "Strong"