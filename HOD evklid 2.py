def NOD(a,b):
	u0 = 1
	v0 = 0
	u1 = 0
	v1 = 1
	while 1 > 0:
		q = a // b
		
		c = a
		a = b
		b = c % b
		
		c = u0
		u0 = u1
		u1 = c - q*u1
		
		c = v0
		v0 = v1
		v1 = c - q*v1
		
		if b == 0:
			return a,u0,v0 
	return a, u0, u1
	
a = int(input())
b = int(input())
gcd,u,v = NOD(a,b)
print('{} = {}*{} + {}*{}'.format(gcd,u,a,v,b))
