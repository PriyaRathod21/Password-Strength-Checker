import string
import getpass

def check_password_strength(password):
    lower_alpha_count = upper_alpha_count = number_count = whitespace_count = special_char_count = 0
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_char_count += 1
    strength = 0
    remarks = ''

    if lower_alpha_count >= 1:
        strength += 1
    if upper_alpha_count >= 1:
        strength += 1
    if number_count >= 1:
        strength += 1
    if whitespace_count >= 1:
        strength += 1
    if special_char_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "This password is extremely weak. Update it immediately to protect your accounts."
    elif strength == 2:
        remarks = "This password is still weak. Consider adding more complexity."
    elif strength == 3:
        remarks = "Your password is okay, but it can be improved by adding more unique elements."
    elif strength == 4:
        remarks = "Well done! Your password is hard to guess. But you can make it even more secure"
    elif strength == 5:
        remarks = "That's a strong password !! This one is nearly uncrackable."

    print("Your password has:-")
    print(f"{lower_alpha_count} lowercase letters")
    print(f"{upper_alpha_count} uppercase letters")
    print(f"{number_count} digits")
    print(f'{whitespace_count} whitespaces')
    print(f"{special_char_count} special characters")
    print(f"Password score: {strength}/5")
    print(f"Remarks: {remarks}")

print("*** Welcome to Password Strength Checker! ***")
while 1:
    choice = input("Do you want to check a password's strength (y/n) : ")
    if 'y' in choice.lower():
        password = getpass.getpass("Enter the password: ")
        check_password_strength(password)
    elif 'n' in choice.lower():
        print('Thanks for using the Password Strength Checker!')
        break
    else:
        print('Invalid input...please try again.')
    print()