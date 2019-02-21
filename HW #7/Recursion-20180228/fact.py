def fact(n):
	if n==0:
		return 1
	else:
		return n * fact(n-1)
		
def main():
	Number=5
	print(fact(Number))

main()