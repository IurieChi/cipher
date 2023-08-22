
text = 'salut'
decoded =''

shift = 0

# text = input("Enter message: ")

def shift_val(shift):
    while shift == 0:
        try:    
            shift = int(input("Enter the cipher shift value (1..25): "))
            if shift not in range(1,26):
                raise ValueError
        except ValueError:
            shift = 0
        if shift == 0:
            print("Incorrect shift value!")# window['erro_shift'].update('Incorrect shift value')
    return shift
 # encrypt data the string sasa

def encode(text, shifting):
    cipher = ''
    for char in text:
        if char.isalpha():
            #shift code 
            code = ord(char) + shifting 
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

# shifting = shift_val(0)
# encode(text,shifting)


# for char in cipher:
#     code = ord(char) -1
#     if code < ord('A'):
#         code = ord('Z')
#     decoded +=chr(code)

# print(decoded)
