'''
Student: Jonathan Medina
Date Completed: October 20th, 2023 [Revised]
Desc: This program purpose is to decipher statements using the Monoalphabetic cipher, however this is further revision
aided with suggestions from my peers
'''
def decrypter(input_letter):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ' + ' ' + '!' + '.')
    cipher_key = list('TIOKGMWBZDEYCJUPFVASHQNRXL' + ' ' + '!' + '.')
    #Above is the keys needed to provide and deciper the message the user will provide

    index = cipher_key.index(input_letter)
    plain_text = alphabet[index]
    #Both of these lines matches the alphabet lines and the cipher to make the program work as intended

    return plain_text

def main():
    #OUJWVTSHYTSZUJ UJ OUCPYGSZJW SBZA OBTYYGJWG! KGOVXPSZJW T OZPBGV SGRS ZA AU CHOB MHJ.
    #Above is the full message if you need to copy and paste for ease of use
    cipher_text = input("Enter your encrypted message: ")
    cipher_text = cipher_text.upper()

    for letter in cipher_text:
        plain_text = decrypter(letter)
        print(plain_text, end="")
    #This for loop runs the decryptor function through the encrypted message that the user provides
main()