# Set the Boolean variables to false.
correct_length = False
has_uppercase = False
has_lowercase = False
has_digitcase = False
length = 7

# input password
password = input('Enter the password: ') 

# Start by testing the
# password's length.
if len(password) >= length:
    correct_length = True

    # Test each character and set the
    # appropriate flag when a required
    # character is found.
    for ch in password:
        if ch.isupper():
            has_uppercase = True
        if ch.islower():
            has_lowercase = True
        if ch.isdigit():
            has_digitcase = True

if has_digitcase and has_lowercase and has_uppercase and correct_length:
    is_valid = True
else:
    is_valid = False

print(f'The is_valid variable: {is_valid}')
