class Vigenere():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))
    
    def __init__(self):
        print("Made a Vigenere")
        

    def printLetters(self):
        for letter in self.index_to_letter:
            print(letter)
            
    def setKey(self, key):
        self.key = key.replace(" ", "")
        
    def encrypt(self, plaintext):
        cipher = ''
        plaintext = plaintext.replace(" ", "")

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

        return cipher
            
    def decrypt(self, ciphertext):
        decrypted = ''

        # Checking if the key is longer and making adjustment if needed
        if (len(self.key) > len(ciphertext)):
            shortened_key = ''
            for letter in range(len(plaintext)):
                shortened_key += self.key[letter]
            self.key = shortened_key


        # Lookup indexes and find corresponding decipher
        index = 0
        for letter in ciphertext:
            number = self.letter_to_index[letter] - self.letter_to_index[self.key[index % len(self.key)]]
            decrypted = decrypted + self.index_to_letter[number % len(self.alphabet)]
            index = index + 1

        return decrypted
        

def main():
    VIG = Vigenere()
    VIG.setKey("APPLE")
    encrypted = VIG.encrypt("BANANA IS THE ENEMY")
    print(encrypted)
    
    print(VIG.decrypt(encrypted))
    
main()
