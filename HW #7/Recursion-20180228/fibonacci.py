def fib(n):
   if n <= 1:
       return n
   else:
   		return(fib(n-1) + fib(n-2))
   		
def main():
	terms = 50
	for i in range(terms):
		print(fib(i))
       
main()