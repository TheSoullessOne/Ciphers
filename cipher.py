######################################################################################
#       To run in command prompt:                                                    #
#       python cipher.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE>     #
######################################################################################
import sys

def main():
    # print command line arguments
    #for arg in sys.argv[1:]:
    #    print(arg)
        
    name = sys.argv[1]
    key = sys.argv[2]
    encOrDec = sys.argv[3]
    inputFile = sys.argv[4]
    outputfile = sys.argv[5]
        
    # If cipher method is Playfair
    if(name == "PLf"):
        cipher = Playfair()
        cipher.setKey(key)
        
        # If ENC
        if(encOrDec == "ENC"):
            cipher.encrypt(inputFile)
        # If DEC
        elif(encOrDec == "DEC"):
            cipher.decrypt(inputFile)
    
    # If cipher method is RowTransposition
    elif(name == "RTS"):
        cipher = RowTransposition()
        cipher.setKey(key)
                
        # If ENC
        if(encOrDec == "ENC"):
            cipher.encrypt(inputFile)
        # If DEC
        elif(encOrDec == "DEC"):
            cipher.decrypt(inputFile)
    
    # If cipher method is Railfence
    elif(name == "RFC"):
        cipher = Railfence()
        cipher.setKey(key)
        
        # If ENC
        if(encOrDec == "ENC"):
            cipher.encrypt(inputFile)
        # If DEC
        elif(encOrDec == "DEC"):
            cipher.decrypt(inputFile)
        
    # If cipher method is Vigenre
    elif(name == "VIG"):
        cipher = Vigenre()
        cipher.setKey(key)
        
        # If ENC
        if(encOrDec == "ENC"):
            cipher.encrypt(inputFile)
        # If DEC
        elif(encOrDec == "DEC"):
            cipher.decrypt(inputFile)
        
    # If cipher method is Caesar
    elif(name == "CES"):
        cipher = Caesar()
        cipher.setKey(key)
        
        # If ENC
        if(encOrDec == "ENC"):
            cipher.encrypt(inputFile)
        # If DEC
        elif(encOrDec == "DEC"):
            cipher.decrypt(inputFile)

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
        
    def setKey(self, key):
        self.key = key
        
    def encrypt(self, plaintext):
        pass
        
    def decrypt(self, ciphertext):
        pass

class RowTransposition(CipherInterface):          # RTS
    def __init__(self):
        CipherInterface.__init__(self)
        print("Made a RowTransposition")
        
    def setKey(self, key):
        self.key = key
        
    def encrypt(self, plaintext):
        pass
        
    def decrypt(self, ciphertext):
        pass

class Railfence(CipherInterface):                 # RFC
    def __init__(self):
        CipherInterface.__init__(self)
        print("Made a Railfence")
        
    def setKey(self, key):
        self.key = key
        
    def encrypt(self, plaintext):
        pass
        
    def decrypt(self, ciphertext):
        pass

class Vigenre(CipherInterface):                   # VIG
    def __init__(self):
        CipherInterface.__init__(self)
        print("Made a Vigenre")
        
    def setKey(self, key):
        self.key = key
        
    def encrypt(self, plaintext):
        pass
        
    def decrypt(self, ciphertext):
        pass

class Caesar(CipherInterface):                    # CES
    def __init__(self):
        CipherInterface.__init__(self)
        
    def setKey(self, key):
        self.key = key
        
    def encrypt(self, plaintext):
        pass
        
    def decrypt(self, ciphertext):
        pass

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