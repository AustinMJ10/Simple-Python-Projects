import re

def assess_password_strength(password):
    # Length Check
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    
    # Uppercase Check
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    
    # Lowercase Check
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."
    
    # Number Check
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one number."
    
    # Special Character Check
    if not re.search("[!@#$%^&*()-+=]", password):
        return "Weak: Password should contain at least one special character."
    
    # Strong Password
    return "Strong: Password meets all criteria."

# Example usage:
password = input("Enter your password: ")
strength = assess_password_strength(password)
print(strength)
