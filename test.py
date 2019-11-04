# python with testing with data types

def F(n: int) -> int:
	if n in (0,1):
		return 1
	else:
		return F(n -1) + F(n - 2)

print('Good use', f(8))
print('Bad use, F(355/133))
