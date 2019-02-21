def fileIngest(fileName):
	inFile = open(fileName, "r")
	return inFile
	inFile.close()
	
def conversionOutput(file):
	numList=[]
	for line in file:		
		full = (line)
		character = (full[0])
		unicode = ord(character)
		hexadecimal = hex(unicode) [2:]
		binary = bin(unicode) [2:]
		output = str("The Character "+str(character)+" is encoded as "+str(unicode)+" in Unicode, which is "+str(hexadecimal)+" in hexadecimal and "+str(binary)+" in binary.")
		numList.append(output)
	return numList
	
def main():
	fileName = "HW5_input.txt"
	conversionFile = fileIngest(fileName)
	conversionCreator = conversionOutput(conversionFile)
	print(str(conversionCreator))
	
		
main()