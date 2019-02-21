def reverse(s):
	if s=="":
		return s
	else:
		return reverse(s[1:])+s[0]
			
def main():
	s="Stranger Things"
	print(reverse(s))

main()


