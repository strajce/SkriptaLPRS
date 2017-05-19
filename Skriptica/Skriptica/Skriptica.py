import sys
import math

T = 2000000
PI = math.pi 

for t0 in range(0,1000000,1):
    p=((2*t0)/T-math.sin((4*PI*t0)/T)/(2*PI))*100
    for i in range(0,99):
        if( p>=i+0.9999 and p<=i+1.0001):
            if( p>=i+0.9999 and p<=i+1.00001):
                if( p>=i+0.99999 and p<=i+1.00001):
                    print("Procenat je ",i+1,"% , vrednost za P je ",p," , T0 je : ",t0)
                else:
                    print("Procenat je ",i+1,"% , vrednost za P je ",p," , T0 je : ",t0)
