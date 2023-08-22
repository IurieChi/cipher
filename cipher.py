# This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during the Gallic Wars.
# The idea is rather simple – every letter of the message is replaced by its nearest consequent 
# Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

# asks the user for one line of text to encrypt;
# asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
# prints out the encoded text.

text = input("Enter your message: ")
shift_value = 0 
cipher = ''
decoded =''

while shift_value ==0:
    try:
        shift_value = int(input('Enter shift value from 1 till 25: '))
        if shift_value not in range(1,26):
            raise ValueError
    except ValueError:
        shift_value = 0
        if shift_value == 0:
            print('Incorrect shift value')

# encrypt data the string 
for char in text:
    if char.isalpha():
        #shift code 
        code = ord(char) + shift_value 
        #find code for first letter   
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        #make corection for first element
        code -=first
        code %=26
        #add encoded element to the message 
        cipher += chr(first + code)
    else:
        cipher += char    
print(cipher)

# for char in cipher:
#     code = ord(char) -1
#     if code < ord('A'):
#         code = ord('Z')
#     decoded +=chr(code)

# print(decoded)
