import sys
import math

T = 2000000
PI = math.pi

file = open("Skriptica1.1.txt","w")

for t0 in range(0,1000000,1):
    p=((2*t0)/T-math.sin((4*PI*t0)/T)/(2*PI))*100
    for i in range(0,99):
        if( p>=i+0.9999 and p<=i+1.0001):
            if( p>=i+0.9999 and p<=i+1.00001):
                if( p>=i+0.99999 and p<=i+1.00001):
                    s=i+1
                    file.write("Procenat = %d " %s)
                    file.write("%")
                    file.write(", vrednost za p = %0.15f " %p)
                    file.write(", t0 = %d " %t0)
                    file.write("\n")
                else:
                    s=i+1
                    file.write("Procenat = %d " %s)
                    file.write("%")
                    file.write(", vrednost za p = %0.15f " %p)
                    file.write(", t0 = %d " %t0)
                    file.write("\n")
            else:
                s=i+1
                file.write("Procenat = %d " %s)
                file.write("%")
                file.write(", vrednost za p = %0.15f " %p)
                file.write(", t0 = %d " %t0)
                file.write("\n")
file.close()
