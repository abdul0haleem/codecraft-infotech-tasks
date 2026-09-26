password = input("Enter your password: ")

score = 0
feedback = []

if len(password) >= 8:
    print("Length requirement: Passed")
    score += 1
else:
    print("Length requirement: Failed")
    feedback.append("Use at least 8 characters.")

if any(char.isupper() for char in password):
    print("Uppercase letter requirement: Passed")
    score += 1
else:
    print("Uppercase letter requirement: Failed")
    feedback.append("Add at least one uppercase letter.")

if any(char.islower() for char in password):
    print("Lowercase letter requirement: Passed")
    score += 1
else:
    print("Lowercase letter requirement: Failed")
    feedback.append("Add at least one lowercase letter.")

if any(char.isdigit() for char in password):
    print("Number requirement: Passed")
    score += 1
else:
    print("Number requirement: Failed")
    feedback.append("Add at least one number.")

if any(not char.isalnum() for char in password):
    print("Special character requirement: Passed")
    score += 1
else:
    print("Special character requirement: Failed")
    feedback.append("Add at least one special character.")

print("Password Strength Score:", score, "/ 5")

if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Moderate")
else:
    print("Password Strength: Strong")

if feedback:
    print("\nSuggestions to improve your password:")
    for suggestion in feedback:
        print("-", suggestion)
else:
    print("\nYour password satisfies all complexity requirements.")
