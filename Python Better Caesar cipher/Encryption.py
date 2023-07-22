def user_input():        #Define our data
    string=input("Please write a one-line text: ")
    move=0
    while move<1 or move>25:
        try:
            move=int(input("Please enter the number in range [1,25] by which the string is to be shifted: "))
        except:
            continue
    return string, move

def encryption(string, move):       #Encrypting our text
    cipher=''
    for char in string:
        if char.isalpha():      #If char is a letter
            ascii=ord(char)+move    
            if ord(char)>=ord('a') and ord(char)<=ord('z'):
                if ascii>122:
                    ascii-=26
            if ord(char)>=ord('A') and ord(char)<=ord('Z'):
                if ascii>90:
                    ascii-=26
            cipher+=chr(ascii)
        elif char.isdigit():        #If char is a digit
            digit=int(char)
            if digit in range(0,9):
                digit+=move
            else:
                digit+=move-10
            while digit>9:      #If digit > 9 we must subtract by 10 while a digit will be in range[0,9]
                digit-=10
            cipher+=str(digit)
            
        else:       #Else we do nothing
            cipher+=char
    return cipher

text, shift=user_input()

print(encryption(text, shift))