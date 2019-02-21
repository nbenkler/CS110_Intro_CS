#benford.py
#	program that reads a file, figures out the frequency of the first digits of each number in the file and determines whether or not the distribution resembles a Benford distribution
# 3/9/18

def fileIngest(fileName):
	inFile = open(fileName, "r")
	return inFile
	inFile.close()
	
def conversionCreator(file):
	dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	for line in file:		
		firstDigit = int (line [0])
		dic [firstDigit] = dic [firstDigit] + 1
	return dic

def benfordTest(dic):
	benford = True
	for i in range (1,8):
		if dic [i] < dic [i+1]:
			benford = False
	return benford

def output(benford):
	if benford == True:
		print("Distribution mirrors a Benford Distribution.")
	else:
		print("Distribution is not a Benford Distribution.")

def main():
	fileName = input("What is the name of the file you would like to read (benfordTEST1.txt of benfordTEST2.txt)? ")
	conversionFile = fileIngest(fileName)
	conversionSetup = conversionCreator(conversionFile)
	conversionResults = benfordTest(conversionSetup)
	conversionEnd =  output(conversionResults)
	

	
main()