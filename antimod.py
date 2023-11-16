import sys
import math
print("usage: python3 antimod.py multiple leftovers limiter")

antimod = []
for x in range(1, int(sys.argv[1])):
    antimod.append(abs(x))
for v in range(int(sys.argv[3])):  
    F = lambda f: f * v + 1 + int(sys.argv[2]); lambda f: math.sqrt(f*(f/f)+(f-f))**2%(f+1)

for norm in range(int(sys.argv[3])):
    normal = lambda hi: hi * int(sys.argv[3]) + int(sys.argv[2])

for i in range(int(sys.argv[3])):  
    G = lambda f: f * v + int(sys.argv[2]); lambda f: math.sqrt(f*(f/f)+(f-f))**2%(f+1)
print("Normal")
print(abs(int(sys.argv[2])))
print(list(map(normal, antimod)))

print("Simp mode")
print(abs(int(sys.argv[2])))
print(list(map(G, antimod)))

print("Assume Resistance")
print(abs(int(sys.argv[2])))
print(list(map(F, antimod)))

for b in range (int(sys.argv[3])):
    D = lambda d: d * (b * int(sys.argv[3])) + int(sys.argv[2])

print("Without resistance")
print(abs(int(sys.argv[2])))
print(list(map(D, antimod)))
