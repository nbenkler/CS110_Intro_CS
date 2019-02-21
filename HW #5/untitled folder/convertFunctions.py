# Program to read file HW5_Input.txt and convert characters in the file to their unicode, hexadecimal, and binary representations.
#Noam Benkler
#2/12/18


def fileIngest(fileName):
	inFile = open(fileName, "r")
	return inFile
	inFile.close()
	
def conversionOutput(file):
	for line in file:		
		full = (line)
		character = (full[0])
		unicode = uniConversion(character)
		hexadecimal = hexConversion(unicode)
		binary = binConversion(unicode)
		output = str("The Character "+str(character)+" is encoded as "+str(unicode)+" in Unicode, which is "+str(hexadecimal)+" in hexadecimal and "+str(binary)+" in binary.")
		print (output)
	
def uniConversion(alphanum):
	uni = ord(alphanum)
	return uni

def hexConversion(alphanum):
	hexa = hex(alphanum) [2:]
	return hexa

def binConversion(alphanum):
	bina = bin(alphanum) [2:]
	return bina
	
def main():
	fileName = "HW5_input.txt"
	conversionFile = fileIngest(fileName)
	conversionOutput(conversionFile)
	
		
main()