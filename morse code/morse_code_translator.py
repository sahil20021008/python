
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

REVERSED_MORSE_CODE_DICT = dict([(value, key) for key, value in MORSE_CODE_DICT.items()])


def encrypt(morse):
    output = ""
    for i in morse:
        if i == " ":
            output += " "
        else:
            output += MORSE_CODE_DICT[i.upper()] + " "
    print("The Morse Code for the given message is:")
    print(output)


def decrypt(morse):
    output = ""
    morse += " "
    blank = 0
    part = ""
    for i in morse:
        if i == " ":
            blank += 1
            if blank == 1:
                output += REVERSED_MORSE_CODE_DICT[part]
                part = ""
            else:
                output += " "
        else:
            blank = 0
            part += i
    print("The decrypted message for the given Morse Code is:")
    print(output)


if __name__ == '__main__':
    print("Enter 1 if you want to encrypt a message in morse code, or press 2 if you want to decrypt a message from "
          "morse code")
    n = int(int(input()))
    if n == 1:
        print("Please enter the message you wish to encrypt")
        message = input()
        encrypt(message)
    elif n == 2:
        print("Please enter the Morse code you wish to decrypt")
        message = input()
        decrypt(message)
    else:
        print("Invalid Input: Please try again")
