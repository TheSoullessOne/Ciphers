def encrypt(key, plaintext):

    key = key.replace(" ", "")
    plaintext = plaintext.replace(" ", "")

    # For extra letters to add to table
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize empty dictionary
    table = {}

    rows = (len(plaintext)//len(key))+1
    cols = len(key)

    # Populate empty dictionary with keys ordered by number of columns
    for i in range(1, cols+1):
        table[i]=[]

    
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
            
    finalResult = ''

    for i in key:
        for j in range(rows):
            finalResult+=table[int(i)][j]

    return finalResult

print(encrypt("3 4 2 1 5 6 7", "attack postponed until two am"))

def decrypt(ciphertext, key):
    key = key.replace(" ", "")
    ciphertext = ciphertext.replace(" ", "")


     # Initialize empty dictionary
    table = {}

    rows = len(ciphertext)//len(key)
    cols = len(key)

    k = 0
     # Populate empty dictionary with columns as the key
    for i in key:
        table[i]=[]
        for j in range(len(ciphertext)):
            if(j>=rows):
                break
            else:
                table[i].append(ciphertext[k])
                k+=1

    new_table = {}

    # Rearrange columns in order 
    for i in range(1, len(key)+1):
        new_table[str(i)]=table[str(i)]

    plaintext = ''

    # Piece the plaintext together by the new table
    for i in range(0, rows):
        for j in range(1, cols+1):
            plaintext+=new_table[str(j)][i]
    
    return plaintext



print(decrypt("ttnaaptmtsuoaodwcoizknlypetx", "3421567"))