def fib(x):
	if x < 0:
		print("Invalid number")
	elif x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)

def fac(x):
	if x < 0:
		print("Invalid number")
	elif x == 0:
		return 1
	else:
		total = 1
		for y in range(1, x + 1):
			total *= y
	return total