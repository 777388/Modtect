import sys
import math
print("usage: python3 antimod.py multiple leftovers limiter")

antimod = []
for x in range(1, int(sys.argv[1])):
    antimod.append(abs(x))
for v in range(int(sys.argv[3])):  
    F = lambda f: f * v + int(sys.argv[2]); lambda f: math.sqrt(f*(f/f)+(f-f))**2%(f+1)

print(abs(int(sys.argv[2])))
print(list(map(F, antimod)))
