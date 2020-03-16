######################################################################################
#       To run in command prompt:                                                    #
#       python cipher.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE>     #
######################################################################################
import sys

def main():
    # print command line arguments
    #for arg in sys.argv[1:]:
    #    print(arg)
    if(len(sys.argv) < 6):
        print("USAGE: " + sys.argv[0] + " <CIPHER> <KEY> <ENC/DEC> <INPUT FILE NAME> <OUTPUT FILE NAME>")
        exit(1)    

    name = sys.argv[1]
    key = sys.argv[2]
    encOrDec = sys.argv[3]
    inputFile = sys.argv[4]
    outputFile = sys.argv[5]
        
    # If cipher method is Playfair
    if(name == "PLF"):
        cipher = PlayFair()
        cipher.setKey(key)
        
        # If ENC
        if(encOrDec == "ENC"):
            cipher.encrypt(inputFile, outputFile, key)
        # If DEC
        elif(encOrDec == "DEC"):
            cipher.decrypt(inputFile, outputFile, key)
    
    # If cipher method is RowTransposition
    elif(name == "RTS"):
        cipher = RowTransposition()
        cipher.setKey(key)
                
        # If ENC
        if(encOrDec == "ENC"):
            cipher.encrypt(inputFile, outputFile)
        # If DEC
        elif(encOrDec == "DEC"):
            cipher.decrypt(inputFile, outputFile)
    
    # If cipher method is Railfence
    elif(name == "RFC"):
        cipher = Railfence()
        cipher.setKey(key)
        
        # If ENC
        if(encOrDec == "ENC"):
            cipher.encrypt(inputFile, outputFile, key)
        # If DEC
        elif(encOrDec == "DEC"):
            cipher.decrypt(inputFile, outputFile, key)
        
    # If cipher method is Vigenre
    elif(name == "VIG"):
        cipher = Vigenere()
        cipher.setKey(key)
        
        # If ENC
        if(encOrDec == "ENC"):
            cipher.encrypt(inputFile, outputFile)
        # If DEC
        elif(encOrDec == "DEC"):
            cipher.decrypt(inputFile, outputFile)
        
    # If cipher method is Caesar
    elif(name == "CES"):
        cipher = Caesar()
        cipher.setKey(key)
        
        # If ENC
        if(encOrDec == "ENC"):
            cipher.encrypt(inputFile, outputFile)
        # If DEC
        elif(encOrDec == "DEC"):
            cipher.decrypt(inputFile, outputFile)

class CipherInterface:                          # Parent Class w/ void functions
    def __init__(self):
        pass
        
    def setKey(self, key):
        self.key = key
        
    def encrypt(self, plaintext):
        pass
        
    def decrypt(self, ciphertext):
        pass
    
    
class PlayFair(CipherInterface):                  # PLF
    def __init__(self):
        CipherInterface.__init__(self)
        print("Made a PlayFair")
    
    def setKey(self, key):                      #create table
        self.key = key

        table = []
        row = []
        index = 0
        alphabet = "abcdefghiklmnopqrstuvwxyz"  #exclude j temporarily
        key = key.replace(" ", "")              # combination of alphabet and key
        key = key.lower()
        key = key + alphabet

        seen = set()
        while index < len(key):

            if not key[index] in seen:
                row.append(key[index])
                seen.add(key[index])
                if len(row) == 5:
                    table.append(row)
                    row = []
            index += 1
        self.table = table

    def do_pair(self, plainText):            #plaintext: bolloon
        index = 0
        pair = ""
        result = []
        while index < len(plainText):
            if pair == "":
                pair = plainText[index]
                index += 1

            elif len(pair) == 1:
                if pair == plainText[index]:
                    pair = pair + 'x'
                else:
                    pair = pair + plainText[index]
                    index += 1

            if len(pair) == 2:
                result.append(pair)
                pair = ""
        if len(pair) == 1:
            pair = pair + 'x'

            result.append(pair)
        return result

    #encryption
    def encrypt(self, inputFile, outputFile, key):
        result =""
        cipherText = []
        inFile = open(inputFile, "r")
        outFile = open(outputFile, "w")    
        inputString = inFile.read()
        inputString = inputString.lower()
        plainText = self.do_pair(inputString)

        m = {}                                #construct coordinate table
        for tRow in range(len(self.table)):
            for tCol in range(len(self.table)):
                m[self.table[tRow][tCol]] = tRow, tCol

        for myWord in plainText:                    #each pair in the new plainText: bo
            l1 = myWord[0]
            l2 = myWord[1]

            if l1 in m:
                (x1, y1) = m.get(l1)
            if l2 in m:
                (x2, y2) = m.get(l2)

            Encl1 = ""
            Encl2 = ""

            #same row
            if x1 == x2:                          
                Encl1 = (x1, (y1 + 1) % 5)
                Encl2 = (x2, (y2 + 1) % 5) 
            #same column
            elif y1 == y2:                        
                Encl1 = ((x1 + 1) % 5, y1)
                Encl2 = ((x2 + 1) % 5, y2)
            #different row and column
            else:                                   
                Encl1 = (x1, y2)
                Encl2 = (x2, y1)

            cipherText.append(self.table[Encl1[0]][Encl1[1]] + self.table[Encl2[0]][Encl2[1]])
        for i in cipherText:
            result += i
        outFile.write(result)

    #Decryption
    def decrypt (self, inputFile, outputFile, key):
        decryptResult = ""
        inFile = open(inputFile, "r")
        outFile = open(outputFile, "w")    
        inputString = inFile.read()

        textToDecrypt = self.do_pair(inputString)
        # table = self.setKey(key)

        decryptedText = []
        m = {}                                #construct coordinate table
        for tRow in range(len(self.table)):
            for tCol in range(len(self.table)):
                m[self.table[tRow][tCol]] = tRow, tCol

        for myWord in textToDecrypt:                    #each pair in the new plainText: bo
            l1 = myWord[0]
            l2 = myWord[1]

            if l1 in m:
                (x1, y1) = m.get(l1)
            if l2 in m:
                (x2, y2) = m.get(l2)

            Encl1 = ""
            Encl2 = ""

            #same row
            if x1 == x2:                          
                Encl1 = (x1, y1 - 1)
                Encl2 = (x2, y2 - 1) 
            #same column
            elif y1 == y2:                        
                Encl1 = (x1 - 1, y1)
                Encl2 = (x2 - 1, y2)
            #different row and column
            else:                                   
                Encl1 = (x1, y2)
                Encl2 = (x2, y1)

            decryptedText.append(self.table[Encl1[0]][Encl1[1]] + self.table[Encl2[0]][Encl2[1]])

        for i in decryptedText:
            decryptResult += i
        outFile.write(decryptResult)

class RowTransposition(CipherInterface):          # RTS
    def __init__(self):
        CipherInterface.__init__(self)
        print("Made a RowTransposition")
        
    def setKey(self, key):
        self.key = key.replace(" ", "")
        
    def encrypt(self, inputfile, outputfile):
        
        # Open input file for reading
        f = open(inputfile, "r")
        plaintext = f.read()
        print(plaintext)
        f.close()

        plaintext = plaintext.replace(" ", "")

        # For extra letters to add to table
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
        # Initialize empty dictionary
        table = {}

        rows = (len(plaintext)//len(self.key))+1
        cols = len(self.key)

        # Populate empty dictionary with keys ordered by number of columns
        for i in range(1, cols+1):
            table[i]=[]

        # Populate contents of the plaintext into the table
        incrementBy = 0
        for i in range(1, cols+1):
            if(incrementBy>=len(plaintext)):
                incrementBy=0
                incrementBy+=i-1
            for j in range(rows):
                if(incrementBy>=len(plaintext)):
                    table[i].append(alphabet.pop())
                else:
                    table[i].append(plaintext[incrementBy])
                    incrementBy+=cols

        # Piece together the final result into a string    
        finalResult = ''

        for i in self.key:
            for j in range(rows):
                finalResult+=table[int(i)][j]
        
        # Write the encrypted contents to the file
        outfile = open(outputfile, "w")

        outfile.write(finalResult)

        outfile.close()
        
        
    def decrypt(self, inputfile, outputfile):

        # Read input file contents
        f = open(inputfile, "r")

        ciphertext = f.read()
        
        f.close()
        
        ciphertext = ciphertext.replace(" ", "")


        # Initialize empty dictionary
        table = {}

        rows = len(ciphertext)//len(self.key)
        cols = len(self.key)

        k = 0
        # Populate empty dictionary with columns as the key
        for i in self.key:
            table[i]=[]
            for j in range(len(ciphertext)):
                if(j>=rows):
                    break
                else:
                    table[i].append(ciphertext[k])
                    k+=1

        # Add new table to rearrange columns in order
        new_table = {}

        # Rearrange columns in order 
        for i in range(1, len(self.key)+1):
            new_table[str(i)]=table[str(i)]

        plaintext = ''

        # Piece the plaintext together by the new table
        for i in range(0, rows):
            for j in range(1, cols+1):
                plaintext+=new_table[str(j)][i]
        
        # Write the decrypted contents to the file
        outfile = open(outputfile, "w")

        outfile.write(plaintext)

        outfile.close()

class Railfence(CipherInterface):                 # RFC
    def __init__(self):
        CipherInterface.__init__(self)
        print("Made a Railfence")
        
    def setKey(self, key):
        self.key = key
        
    def encrypt(self, inputFile, outputFile, key):          #meetmeafterthetogaparty
        inFile = open(inputFile, "r")
        outFile = open(outputFile, "w")
        keyRow = 0
        plainText = inFile.read()
        plainText = plainText.lower()

        result = ""
        rowResult = ""
        temp = 0
        keyRow = 0

        for i in plainText:                               #strip all spaces if present
            if i == " ":
                plainText = plainText.replace(i, "")
        
        while keyRow < int(key):
            while temp < len(plainText):
                rowResult = rowResult + plainText[temp]
                temp = temp + int(key)
            keyRow = keyRow + 1
            temp = keyRow
            result = result + rowResult
            rowResult = ""

        outFile.write(result)
        inFile.close()
        outFile.close()
        
    def decrypt(self, inputFile, outputFile, key):
        inFile = open(inputFile, "r")
        outFile = open(outputFile, "w")
        plainText = inFile.read()

        myList = []
        tempString = plainText
        index = 0
        letterPerRow = int(len(plainText) / int(key))
        extraLetters = int(len(plainText) % int(key))

        #create a list of rows of letters
        while index < int(key):
            if extraLetters > 0:
                myList.append(tempString[:letterPerRow + 1])
                tempString = tempString[letterPerRow+1:]
                extraLetters -= 1
            else:
                myList.append(tempString[:letterPerRow])
                tempString = tempString[letterPerRow:]
            index += 1

        row = 0
        col = 0
        tempString = ""
        result = ""
        extraLetters = int(len(plainText) % int(key))
        
        #start decrypting
        while col < letterPerRow:
            while row < int(key):
                tempString = tempString + myList[row][col]
                row += 1
            col += 1
            row = 0
            result += tempString
            tempString = ""
            
        #fill up with extra letters
        if extraLetters > 0:
            i = 0
            while i < extraLetters:
                result += myList[i][letterPerRow]
                i += 1

        outFile.write(result)
        inFile.close()
        outFile.close()

class Vigenere():
    # Mapping alphabet and letter indexes
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))
    
    def __init__(self):
        print("Made a Vigenere")
        
    def setKey(self, key):
        self.key = key.replace(" ", "")
        
    def encrypt(self, infile, outfile):
        # Read in the plaintext as a string and replace whitespace and newlines
        with open(infile, 'r') as file:
            plaintext = file.read().replace('\n', '')
        plaintext = plaintext.replace(" ", "")
        plaintext = plaintext.upper()
        cipher = ''

        # Checking if the key is longer than the plaintext
        # and updating the key to match the length
        if (len(self.key) > len(plaintext)):
            shortened_key = ''
            for letter in range(len(plaintext)):
                shortened_key += self.key[letter]
            self.key = shortened_key

        # Lookup indexes and find corresponding cipher
        index = 0
        for letter in plaintext:
            number = self.letter_to_index[letter] + self.letter_to_index[self.key[index % len(self.key)]]
            cipher += self.index_to_letter[number % len(self.alphabet)]
            index = index + 1

        # Write out the file
        outfile = open(outfile, "w")
        outfile.write(str(cipher))
            
    def decrypt(self, infile, outfile):
        # Read the ciphertext into a string while replacing all whitespace and newlines
        with open(infile, 'r') as file:
            ciphertext = file.read().replace('\n', '')
        ciphertext = ciphertext.replace(" ", " ")
        ciphertext = ciphertext.upper()
        decrypted = ''

        # Checking if the key is longer and making adjustment if needed
        if (len(self.key) > len(ciphertext)):
            shortened_key = ''
            for letter in range(len(ciphertext)):
                shortened_key += self.key[letter]
            self.key = shortened_key


        # Lookup indexes and find corresponding decipher
        index = 0
        for letter in ciphertext:
            number = self.letter_to_index[letter] - self.letter_to_index[self.key[index % len(self.key)]]
            decrypted = decrypted + self.index_to_letter[number % len(self.alphabet)]
            index = index + 1

        # Write out decrypted file
        outfile = open(outfile, "w")
        outfile.write(decrypted)

class Caesar(CipherInterface):                    # CES
    def __init__(self):
        CipherInterface.__init__(self)
        
    def setKey(self, key):
        self.key = key
        
    def encrypt(self, infile, outfile):
        with open(infile, 'r') as file:
            ciphertext = file.read().replace('\n', '')

        ciphertext = ciphertext.replace(" ", " ")
        result = ''

        for char in ciphertext:
            if char.isalpha():
                newChar = chr(ord(char) + int(self.key))
                while ord(newChar) > 122:
                    newChar = chr(ord(newChar) - 26)
                print(ord(newChar))
                result += newChar

        outfile = open(outfile, "w+")
        outfile.write(result)
        outfile.close()

    def decrypt(self, infile, outfile):
        with open(infile, 'r') as file:
            ciphertext = file.read().replace('\n', '')

        ciphertext = ciphertext.replace(" ", " ")
        result = ''

        for char in ciphertext:
            if char.isalpha():
                result += chr(ord(char) - int(self.key) % 26)
        
        outfile = open(outfile, "w+")
        outfile.write(result)
        outfile.close()

##################################### EXTRA CREDIT ########################################
class Hill(CipherInterface):                      # HIL
    def __init__(self, CipherInterface):
        CipherInterface.__init__(self)
        
    def setKey(self, key):
        self.key = key
        
    def encrypt(self, plaintext):
        pass
        
    def decrypt(self, ciphertext):
        pass

class ThreeRotorEnigma(CipherInterface):          # 3RE
    def __init__(self, CipherInterface):
        CipherInterface.__init__(self)
        
    def setKey(self, key):
        self.key = key
        
    def encrypt(self, plaintext):
        pass
        
    def decrypt(self, ciphertext):
        pass

if __name__== "__main__":
    main()
