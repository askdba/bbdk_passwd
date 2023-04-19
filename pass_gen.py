import sys
import random

def generate_password(num, prev_passwords):
    # Check that the input number is a 6-digit number
    if not (isinstance(num, str) and len(num) == 6 and num.isdigit()):
        print('Error: Input must be a 6-digit number.')
        sys.exit(1)

    # Convert the input number to a list of digits
    digits = list(num)

    # Add a random number between 0 and 9 to each of the first three digits
    for i in range(3):
        digits[i] = str((int(digits[i]) + random.randint(0, 9)) % 10)

    # Add a random number between 0 and 9 to each of the last three digits
    for i in range(3):
        digits[i+3] = str((int(digits[i+3]) + random.randint(0, 9)) % 10)

    # Join the digits back into a single string and convert to an integer
    password = int(''.join(digits))

    # Check if the password has been generated before
    while password in prev_passwords:
        # If it has, generate a new password
        password = generate_password(num, prev_passwords)

    # Add the new password to the list of previous passwords
    prev_passwords.append(password)

    return password

if __name__ == '__main__':
    # Load the previous passwords from the file
    with open('prev_passwords.txt', 'r') as f:
        prev_passwords = [int(line.strip()) for line in f]

    # Check that the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print('Usage: python generate_password.py <6-digit number>')
        sys.exit(1)

    # Get the input argument from the command line
    num = sys.argv[1]

    # Generate a new password
    password = generate_password(num, prev_passwords)

    # Save the updated list of previous passwords to the file
    with open('prev_passwords.txt', 'a') as f:
        f.write(str(password) + '\n')

    # Print the new password to the console
    print(password)

