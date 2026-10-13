import string
import secrets

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "admin", "iloveyou", "welcome"
}

def generate_strong_password(length=16):
    """Generate a random password containing different character types."""
    if length < 8:
        length = 8

    characters = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + "!@#$%^&*()-_=+"
    )

    # Ensure at least one character from each category.
    password_chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*()-_=+")
    ]

    password_chars += [
        secrets.choice(characters) for _ in range(length - 4)
    ]

    # Securely shuffle the characters.
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if any(ch.islower() for ch in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    if any(ch.isupper() for ch in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    if any(ch.isdigit() for ch in password):
        score += 1
    else:
        suggestions.append("Add numbers (0-9).")

    if any(ch in string.punctuation for ch in password):
        score += 1
    else:
        suggestions.append("Add a special character, such as ! or #.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append("Avoid common passwords.")

    if len(password) < 8:
        strength = "Very Weak"
    elif score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    elif score <= 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, suggestions


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH ANALYZER")
    print("=" * 40)

    password = input("Enter a test password: ")

    strength, suggestions = analyze_password(password)

    print("\nPassword strength:", strength)

    if suggestions:
        print("\nSuggestions to improve:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Good job! Your password meets these basic checks.")

    print("\nGenerated stronger alternative:")
    print(generate_strong_password())

    print("\nSecurity tip: Never share your real password.")
    print("This demo does not save or transmit your password.")


if __name__ == "__main__":
    main()
