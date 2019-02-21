#conversion1.py
#	A program to convert Celsius temps to Fahrenheit


def main():
	fileName = eval(input("What is the name of the file you would like to convert? "))		
	inFile = open(fileName, "r")	
	for line in inFile:
		celsius = int(line)
		fahrenheit = 9/5 * celsius + 32
		print(celsius, "degrees celsius is", fahrenheit, "degrees in Fahrenheit.")
	inFile.close()
	
main()	


	
