#from fractions import Fraction
#from decimal import Decimal
import math
A,B = map(float,input().split())

tmp = A*B
#tmp = Decimal(A)*Decimal(B)
print(int(math.floor(tmp)))
