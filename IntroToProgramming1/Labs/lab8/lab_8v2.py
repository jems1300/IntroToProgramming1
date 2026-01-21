'''
Name: Jonathan Medina
Date Completed: 10/26/2023
Desc: This program sorts three given inputs from the user in either alphabetical or numerical order
'''

def sort_two_numbers(num1, num2):
    if num1 > num2:
        temp = num1
        num1 = num2
        num2 = temp
    return num1, num2
'''
From what I understand, this function makes sure that the numbers are in order, and temp makes sure that numbers 
aren't replaced permanently since there's so many values to juggle within this program. It's a safer way to execute this
function
'''
def sort_numbers(num1, num2, num3):
    num1, num2 = sort_two_numbers(num1, num2)
    num2, num3 = sort_two_numbers(num2, num3)
    num1, num2 = sort_two_numbers(num1, num2)
    return num1, num2, num3
    #The return value, as well in the other functions below makes the output available to other functions like main
    #Without it, we wouldn't be able to produce an output

def sort_two_strings(word1, word2):
    if word1 > word2:
        temp = word1
        word1 = word2
        word2 = temp
    return word1, word2

def sort_strings(word1, word2, word3):
    word1, word2 = sort_two_strings(word1, word2)
    word2, word3 = sort_two_strings(word2, word3)
    word1, word2 = sort_two_strings(word1, word2)
    return word1, word2, word3
'''
And like sort_numbers above, these 2nd functions repeat the primary functions three times, instead of copy pasting
sort_strings and sort_numbers three times each which caused an error in my previous attempts. Now that these variables 
are sorted, it's stored in each variable respectively and ready to be used for the main function to be called 
'''

def main():
    try:
        user = int(input("Enter 1 for numbers, or 2 for words: "))
        if user == 1:
            num1 = int(input("Please enter the 1st number: "))
            num2 = int(input("Please enter the 2nd number: "))
            num3 = int(input("Please enter the 3rd number: "))
            print("Original Numbers: ", num1, num2, num3)
            print("Sorted Numbers: ", *sort_numbers(num1, num2, num3))
            # And now the purpose of the previous functions come into action, I recall sort_numbers to display the sorted numbers
            # The asterisk is added since I wanted to remove the parenthesis from the output, thanks Google!
        #Like previous labs, a simple elif-if statement depending on what the user picks
        elif user == 2:
            word1 = str(input("Please enter the 1st word: "))
            word2 = str(input("Please enter the 2nd word: "))
            word3 = str(input("Please enter the 3rd word: "))
            print("Original Statement: ", word1, word2, word3)
            print("Sorted Statement: ", *sort_strings(word1, word2, word3))
    # This is a repeat of the previous statement but with strings instead, working properly
    except Exception:
        print("Your input was invalid, please try again")
    # I was not able to get this work if user inputs 4 or bigger numbers
main()

