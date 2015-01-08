trueAlphabet = 'abcdefghijklmnopqrstuvwxyz'
shiftedAlphabet = 'defghijklmnoqprstuvwxyzabc'
plainText = 'hello'
cipherText = ''

for letter in plainText:
    position = trueAlphabet.index(letter)
    shiftedLetter = shiftedAlphabet[position]
    cipherText = cipherText + shiftedLetter
print(cipherText)
