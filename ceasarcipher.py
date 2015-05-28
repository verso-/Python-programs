#Sam Verma
#ceasar cipher
#user enters a message to encrypt or decrypt with a number key

KEY_MAX=26

#asks the user whether they want to encrypt or decrypt 
def getOption():
    print('Do you want to encrypt or decrypt a message?')
    option=input().lower()
    if option in 'encrypt e decrypt d'.split():
        return option
    else:
        print('Enter either "encrypt" or "e" or "decrypt" or "d".')

#asks the user for the message to be translated 
def getMsg():
    print('Enter your message:')
    return input()

#asks the user for the number key
def getKey():
    key=0
    while True:
        print('Enter the key number (1-%s)'%(KEY_MAX))
        key=int(input())
        if(key>=1 and key<=KEY_MAX):
              return key

#translates the message
def getTranslation(option,msg,key):
    if option[0]=='d':
        key=-key              #if the option is to decrypt, the key is inve
    translated=''

    for symbol in msg:
        if symbol.isalpha():  #checks if the character in the msg is a letter
            num=ord(symbol)   #converts it to the ordinal value
            num+=key          #adds the key to it

            if symbol.isupper():   #if the character's uppercase checks if it's
                if num>ord('Z'):   #ord is > ord('Z') so it can 'wrap around'
                    num-=26        
                elif num<ord('A'): #does the same thing if ord < ord('A')
                    num+=26
            elif symbol.islower(): #if the character's lowercase then compares to ord for z and a
                if num>ord('z'):
                    num-=26
                elif num<ord('a'):
                    num+=26

            translated+=chr(num) #creates the translated string by adding unchanged chars if they're not letters and changed ones if they are
        else:
            translated+=symbol
    return translated          #returns the translated msg

option=getOption()
msg=getMsg()
key=getKey()

print('The translated text is:')
print(getTranslation(option,msg,key))              
