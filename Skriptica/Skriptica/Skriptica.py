import sys
import math

T = 2000000
PI = math.pi

# int -> frac
fracs = []
counts = []

for i in range(0,101):
    fracs.append(1000)
    counts.append(-1)

file = open("SkripticaHexa.txt","w")

for t0 in range(0,1000000,1):
    p=((2*t0)/T-math.sin((4*PI*t0)/T)/(2*PI))*100
    i = round(p)
    f = abs(p-i)
    if f<fracs[i]:
        fracs[i] = f
        counts[i] = t0

for i in range(0,101):
    file.write("%d " %i +'=> x"'+'%08x"'%counts[i] + ",\n")
file.close()
