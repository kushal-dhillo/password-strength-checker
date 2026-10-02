# Password Strength Checker

password = input("Enter your password: ")

length = len(password)
uppercase = False
lowercase = False
number = False
special = False

for char in password:
    if char.isupper():
        uppercase = True
    elif char.islower():
        lowercase = True
    elif char.isdigit():
        number = True
    else:
        special = True

score = 0

if length >= 8:
    score += 1

if uppercase:
    score += 1

if lowercase:
    score += 1

if number:
    score += 1

if special:
    score += 1

# Display result
print("\n--- Password Strength Result ---")

if score <= 2:
    print("Strength: WEAK")
elif score <= 4:
    print("Strength: MEDIUM")
else:
    print("Strength: STRONG")

print("\nFeedback:")

if length < 8:
    print("- Use at least 8 characters.")
if not uppercase:
    print("- Add an uppercase letter.")
if not lowercase:
    print("- Add a lowercase letter.")
if not number:
    print("- Add a number.")
if not special:
    print("- Add a special character like @, #, $, !.")

if score == 5:
    print("- Your password meets all the basic security requirements!")
