# Program to read file Assignment7_input.txt and convert numbers in the file to their binary representations then print out conversions in a list
#Noam Benkler
#2/28/18


def fileIngest(fileName):
	inFile = open(fileName, "r")
	return inFile
	inFile.close()
	
def fileProcess(file):
	binaryList=[]
	for line in file:		
		character = int(line)
		binary = binaryRecursiveConversion(character)
		output = str("The decimal number "+ str(character) + " is " + str(binary) +" in binary.\n")
		binaryList.append(output)
	return binaryList
	
def binaryRecursiveConversion(alphanum):
	if alphanum == 0:
		return 0
	else:
		return(alphanum % 2 + 10 * binaryRecursiveConversion(int(alphanum / 2)))

def fileOutput(conversionList):
	outFile = open('convertedDecimals.txt', "w")
	for i in conversionList:
		outFile.write(i)
	outFile.close()		

def main():
	fileName = "Assignment7_input.txt"
	conversionFile = fileIngest(fileName)
	conversionResults = fileProcess(conversionFile)
	fileOutput(conversionResults)
		
main()