# Author: Andrew Thompson

# Description: Application for encrypting and decrypting Strings using a columnar transposition.
#
#
# Currently working on the functionality of the GUI
#



import random
from appJar import gui

def generateKey(raw_key): #return permutation with no duplicates
    acc=''
    acc1=''
    acc2=''
    key=''
    for i in range(1,len(raw_key)+1): #reverse the raw_key in order to eliminate all duplicates
        acc=acc+raw_key[-i]
    for ch in acc: #eliminate duplicates
        if ch not in acc1:
            acc1=acc1+ch
    for j in range(1,len(acc1)+1): #reverse back to original order
        acc2=acc2+acc1[-j]
    for ch1 in acc2: #create permutation
        count=0
        for newch1 in acc2:
            if newch1<ch1:
                count=count+1
        key=key+str(count+1)
    return(key)

def toPlaintext(s,keyLength): #eliminate anything but letters and make uppercase, add random letters to fill last row
    s = s.upper()
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for ch in s: #eliminate anything that is not a letter
        if ch not in upper:
            s = s.replace(ch,'')
    intermediate = s
    if len(intermediate)%keyLength != 0: #add random letters to fill last row
        numLetters = keyLength - len(intermediate)%keyLength
        for i in range(numLetters):
            index = random.randint(0,25)
            intermediate = intermediate + upper[index]
    return(intermediate)

    
def columnar(plaintext,key): #construct ciphertext using columnar transposition
    acc = ''
    listInt = []
    finalList = []
    order = []
    keyLength = len(key)
    for i in range(len(key)): #create a list from key
        listInt.append(int(key[i]))
        finalList.append(int(key[i]))
    for i in range(len(listInt)): #order the list from key
        order.append(min(listInt))
        listInt.remove(min(listInt))
    for item in order: #add columns in order to accumulator
        for i in range(len(plaintext)//keyLength):
            acc = acc + plaintext[finalList.index(item)+(keyLength*i)]
    return(acc)


def encryptColumnar(s,raw_key): #combine all other functions to complete encryption
    key = generateKey(raw_key)
    keyLength = len(key)
    plaintext = toPlaintext(s,keyLength)
    ciphertext = columnar(plaintext,key)
    return(ciphertext)

def decryptColumnar(ciphertext,raw_key):
    acc = ''
    listInt = []
    finalList = []
    order = []
    key = generateKey(raw_key)
    keyLength = len(key)
    copyCipher = ''
    for i in range(keyLength):
        copyCipher = copyCipher + ciphertext[(len(ciphertext)//keyLength)*i:(len(ciphertext)//keyLength)*(i+1)] + ' ' #separate original columns into a list
    listCipher = copyCipher.split(' ')
    for i in range(len(key)): #create a list from key
        listInt.append(int(key[i]))
        finalList.append(int(key[i]))
    for i in range(len(listInt)): #order the list from key
        order.append(min(listInt))
        listInt.remove(min(listInt))
    for i in range(len(ciphertext)//keyLength): #create a string with the letters put back into order
        for item in finalList:
            acc = acc + listCipher[order.index(item)][i]
    return(acc) #print plaintext


app = gui('main window', '800x400')  # create main user window
app.setFont(20)

app.addLabel("title", "Welcome to columnar cryptographer!")
app.setLabelBg("title","white")

app.addLabel('question',"Would you like to encrypt or decrypt?")
app.setLabelBg('question', 'white')

def press(button): # define user event 
    if button == "Encrypt":
        app.stop()
        encryptApp = gui('encrypt window', '800x400') # create new window for encryption
        encryptApp.addLabelEntry('Enter text for encryption: (letters only, no numbers allowed)')
        encryptApp.addLabelEntry('Enter key for encryption: (can be mix of letters and numbers)')

        encryptApp.setFocus('Enter text for encryption: (letters only, no numbers allowed)') # put cursor in label by default

        
        encryptApp.setFont(20)

        def submitEncrypt(button): # define user event
            encryptText = encryptApp.getEntry('Enter text for encryption: (letters only, no numbers allowed)') # get entries that user inputs
            encryptKey = encryptApp.getEntry('Enter key for encryption: (can be mix of letters and numbers)')
            
            encryptApp.stop()
            
            resultsEncrypt = gui('results encrypt', '800x400') # create new window for results
            resultsEncrypt.addSelectableLabel('results', 'Encrypted result: ' + encryptColumnar(encryptText, encryptKey))
            resultsEncrypt.setLabelBg('results', 'white')
            resultsEncrypt.setFont(20)
            resultsEncrypt.go()

        encryptApp.addButton('Submit', submitEncrypt) # create button for submitting encryption
        encryptApp.go()
        
    else:
        app.stop()
        decryptApp = gui('decrypt window', '800x400') # create new window for decryption
        decryptApp.addLabelEntry('Enter text for decryption:')
        decryptApp.addLabelEntry('Enter key for decryption:')

        decryptApp.setFocus('Enter text for decryption:')
        
        decryptApp.setFont(20)
        
        def submitDecrypt(button): # define user event
            decryptText = decryptApp.getEntry('Enter text for decryption:') # get entries that user input
            decryptKey = decryptApp.getEntry('Enter key for decryption:')
            
            decryptApp.stop()

            resultsDecrypt = gui('results decrypt', '800x400') # create new window for results
            resultsDecrypt.addLabel('results', 'Decrypted result: ' + decryptColumnar(decryptText, decryptKey))
            resultsDecrypt.setLabelBg('results', 'white')
            resultsDecrypt.addLabel('disclaimer', 'Please be aware that all spaces have been removed')
            resultsDecrypt.setLabelBg('disclaimer', 'white')
            resultsDecrypt.setFont(20)
            resultsDecrypt.go()

        decryptApp.addButton('Submit', submitDecrypt) # create button for submitting decryption
        decryptApp.go()


app.addButtons(["Encrypt", 'Decrypt'], press) # add encryption and decryption buttons to main window


app.go()

    
