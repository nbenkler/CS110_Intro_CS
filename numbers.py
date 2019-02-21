#Noam Benkler     1/14/18
#numbers.py
#program determines whether integer is zero, positive, or negative; even, odd, or prime; and what the number is multiplied by pi

def main():

	numberText = input('Input an integer, please: ')
	num = int(numberText)
	
	if num > 0:
		print ('number is positive')
	elif num == 0:
		print ('number is zero')
	else:
		print ('number is negative')
	
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				print ('your number is even' if (-1)**num==1 else 'your number is odd')
				break
		else:
			print ('your number is prime')	
			
	if num == 1:
		print ('your number is prime')
		
	if (-num) > 1:
		for i in range(2,(-num)):
			if ((-num) % i) == 0:
				print ('your number is even' if (-1)**(-num)==1 else 'your number is odd')
				break
		else:
			print ('your number is prime')	
	
	if num == -1:
		print ('your number is prime')
	
	print ('number multiplied by pi is', num*3.14159)
	
main()