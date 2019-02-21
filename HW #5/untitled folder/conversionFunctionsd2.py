#conversion3.py
#	Another program to convert Celsius temps to Fahrenheit

def fileIngest(fileName):
	inFile = open(fileName, "r")
	return inFile
	inFile.close()
	
def conversionCreator(file):
	numList=[]
	for line in file:		
		full = (line)
		character = (full[0])
		unicode = ord(character)
		hexadecimal = hex(unicode)
		binary = bin(unicode)
		output = str(str(character)+" is encoded as "+str(unicode)+" in Unicode, which is "+str(hexadecimal)+" in hexadecimal and "+str(binary)+" in binary.")
		numList.append(output)
	return numList

def fileOutput(conversionList):
	outFile = open('unihexabinList.txt', "w")
	outFile.write(conversionList)
	outFile.close()	

def main():
	fileName = "HW5_input.txt"
	conversionFile = fileIngest(fileName)
	conversionOutput = conversionCreator(conversionFile)
	fileOutput(str(conversionOutput))

	
main()