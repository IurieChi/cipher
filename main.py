import PySimpleGUI as sg


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
    return cipher 

def decode(cipher, shifting):
    text = ''
    for char in cipher:
        if char.isalpha():
            #shift code 
            code = ord(char) - shifting 
            #find code for first letter   
            if char.isupper():
                first = ord('A')
            else:
                first = ord('a')
            #make corection for first element
            code -=first
            code %=26
            #add encoded element to the message 
            text += chr(first + code)
        else:
            text += char    
    return text

layout =[
[sg.Text('Shift value from 1 till 25:'), sg.Input(key='shift_value', size=(4,1))],
[sg.Text(size=(40,1), key='erro_shift')],
[sg.Text('Message', size=(49,1)) ,sg.Text('Encrypted/Decrypted Message')],
[sg.Multiline(key='text', size=(45,30)),sg.Multiline(key='result', size=(45,30))],
[sg.Button('Encrypt'), sg.Button('Decrypt'), sg.Button('Copy')],
[sg.Button('Exit')],
]

window = sg.Window('Message encription / decription ', layout)  #sg.theme('dark grey 9')



while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Encrypt':
        shifts = values['shift_value']
        if shifts.isnumeric():
            shifts = int(shifts)
            if shifts not in range(1,26):
                window['erro_shift'].update(f'Shift {shifts} not in range from 1..25!',text_color='red')
            else:
               result =  encode(values['text'],shifts)
               window['result'].update(result)
        else:
            window['erro_shift'].update(f'Incorrect shift value!')

    if event == 'Decrypt':
        shifts = values['shift_value']
        if shifts.isnumeric():
            shifts = int(shifts)
            if shifts not in range(1,26):
                window['erro_shift'].update(f'Shift {shifts} not in range from 1..25!',text_color='red')
            else:
               result =  decode(values['text'],shifts)
               window['result'].update(result)
        else:
            window['erro_shift'].update(f'Incorrect shift value!')
    if event == 'Copy':
        pass

window.close()


