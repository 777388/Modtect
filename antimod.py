import sys
print("usage: python3 antimod.py multiple leftovers")

antimod = []
for x in range(int(sys.argv[1])):
    antimod.append(x)
for v in range(int(sys.argv[1])):  
    F = lambda f: f * v + int(sys.argv[2])

print(list(map(F, antimod)))