# Write a progam that takes an integer keyed in from the terminal and extracts and displays
# each digit of the integer in English. So, if the user types in 932, the program should display
# nine three two. Remember to display "zero" if the user types in just a 0. 
# (Note: This exercise is a hard one!)

def main():
    userNumber = raw_input('Enter your number in integer form: ')
    print userNumber
    numConvert(userNumber)
    return

def numConvert(userNumber):
    numWord = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 0: 'Zero'}
    number = userNumber[0]
    print number
    
main()

print '\n'
input('Press enter to exit.')