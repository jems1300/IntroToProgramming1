'''
Student: Jonathan Medina
Date Completed: October 20th, 2023 (Might be revised)
Desc: This program purpose is to decipher statements using the Monoalphabetic cipher
'''
def main():
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ' + ' ' + '!' + '.')
    cipher_key = list('TIOKGMWBZDEYCJUPFVASHQNRXL' + ' ' + '!' + '.')
    #I created these two lines with the list function to be able work with the commands below

    print(f"alphabet: {alphabet}")
    print(f"cipher  : {cipher_key}")
    #This simply prints out the keys, making them match exactly with each other visually for reference

    cipher_text = input("Enter the message you want to decrypt: ")
    cipher_text = cipher_text.upper()
    #This forces any input that was made typed in lower case to upper case
    plain_text = ""

    for i in cipher_text:
        index = cipher_key.index(i)
        plain_text += alphabet[index]
        #The most important lines in this function is the index line, basically determing which letter matches with what
        #and the cipher vice versa
    print("Encrypted message: ", cipher_text)
    print("Plain message: ", plain_text)
main()