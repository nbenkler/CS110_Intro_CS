#conversion2.py
#	Another program to convert Celsius temps to Fahrenheit

def fileIngest(fileName):
	inFile = open(fileName, "r")
	return inFile
	inFile.close()
	
def conversionCreator(file):
	for line in file:
		celsius = int(line)
		fahrenheit = conversion(celsius)
		print(celsius, "degrees celsius is", fahrenheit, "degrees in Fahrenheit.")

def conversion(c_temp):
	f_temp =  9/5 * c_temp + 32
	return f_temp	

def main():
	fileName = eval(input("What is the name of the file you would like to convert? "))
	conversionFile = fileIngest(fileName)
	conversionCreator(conversionFile)

	
main()