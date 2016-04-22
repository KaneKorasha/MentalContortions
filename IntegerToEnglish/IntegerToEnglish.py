# Write a progam that takes an integer keyed in from the terminal and extracts and displays
# each digit of the integer in English. So, if the user types in 932, the program should display
# nine three two. Remember to display "zero" if the user types in just a 0. 
# (Note: This exercise is a hard one!)

def main():
    userNumber = raw_input('Enter your number in integer form: ')
    loopNumber(userNumber)
    return

def loopNumber(userNumber):
    finalNumber = ''
    while userNumber != '':
        #print userNumber
        numWord = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', \
               '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '0': 'zero'}
        number = userNumber[0]
        stringNumber = numWord[number]
        finalNumber = finalNumber + ' ' + stringNumber
        userNumber = userNumber[1:]
    print finalNumber
    return

def numConvert(userNumber, finalNumber):

    #print userNumber
    return userNumber, finalNumber
    
main()

print '\n'
exit = raw_input('Press enter to exit.')
