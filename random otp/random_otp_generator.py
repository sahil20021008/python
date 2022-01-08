import random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if __name__ == '__main__':
    otp = ""
    for i in range(6):
        otp += random.choice(DIGITS)
    print("Your random 6-digit otp is", otp)
