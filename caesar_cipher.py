
LAST_CHAR=ord("Z")#all caps indicate that nothing should be changed
FIRST_CHAR=ord("A")
CHAR_RANGE=LAST_CHAR-FIRST_CHAR+1


def ceasar_shift(message,shift):
    result=""
    #go through each letter in the message
    for char in message.upper():
        if char.isalpha():  #A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.


        #convert character to ascii code
            char_code=ord(char)#Return the Unicode code point for a one-character string.
            new_char_code=char_code+shift
            if new_char_code>LAST_CHAR:
                new_char_code-=CHAR_RANGE
            
            if new_char_code<FIRST_CHAR:
                new_char_code += CHAR_RANGE
            new_char=chr(new_char_code)
            result+=new_char
        else:
            result=result +char
    print(result)


user_message=input("Message to encrypt: ")
user_key=int(input("Shift key:"))
ceasar_shift(user_message,user_key)


