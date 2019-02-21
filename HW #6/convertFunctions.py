# convertFunctions.py
# Noam Benkler 2/19/18
# program that translates number inputed between 1 and 12 to corresponding Month

def monthTest():
    numbersList = [4, 10]
    monthsList = ['April', 'October']
    testList = []
    for i in range (len(numbersList)):
        testList.append(monthConversion(numbersList[i]))
    print ("test list =", testList)
    print ("Months list =", monthsList)
    if testList == monthsList:
        return True
    else:
        return False

def monthConversion(n):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months [n-1]

def userInput():
    n = int(input("Enter a number between 1 and 12: "))
    if n <= 12:
        return n
    else:
        print ("Your number was greater than 12, please enter a number between 1 and 12.")
        exit()

def main():
    if monthTest () == False:
        print ("Experiencing technical dificulties. Quitting program")
        exit()
    n = userInput()
    print(monthConversion(n))
    
main()