#conversion3.py
#	Another program to convert Celsius temps to Fahrenheit

def fileIngest(fileName):
	inFile = open(fileName, "r")
	return inFile
	inFile.close()
	
def conversionCreator(file):
	fahrenheitList=[]
	for line in file:		
		celsius = int(line)
		fahrenheit = conversion(celsius)
		output = str(str(celsius)+" degrees celsius is "+str(fahrenheit)+" degrees in Fahrenheit.")
		fahrenheitList.append(output)
	return fahrenheitList

def fileOutput(conversionList):
	outFile = open('fahrenheitTemps.txt', "w")
	outFile.write(conversionList)
	outFile.close()	

def conversion(c_temp):
	f_temp =  9/5 * c_temp + 32
	return f_temp	

def main():
	fileName = eval(input("What is the name of the file you would like to convert? "))
	conversionFile = fileIngest(fileName)
	conversionResults = conversionCreator(conversionFile)
	fileOutput(str(conversionResults))

	
main()