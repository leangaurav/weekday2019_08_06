import sys

if len(sys.argv) == 3:
	if(sys.argv[1].isdigit() and  sys.argv[2].isdigit()):
		print(int(sys.argv[1])+ int(sys.argv[2]))
	else:
		print("Enter numbers only")
		
else:
	print("Invalid numbers")
