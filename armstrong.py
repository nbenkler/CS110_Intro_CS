#Algorithm that reads a file of numbers and calculates whether or not those numbers are armstrong numbers
#Noam Benkler
#1/27/18



def main():
	F= open("armstrongTestNumbers.txt", "r")
	for line in F:
		Len=len(line) 
		ad=0
		for i in range(Len-1):
			num=int(line[i])
			four=(num**(Len-1))
			ad=four+ad
		if ad == int(line):
			print (line, ' is an Armstrong Number')
		
	F.close()

main()



 