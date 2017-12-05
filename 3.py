import sys

X = int(sys.argv[1])
mi = 1
ma = 1
l = 0
for i in range(1, 1000, 2):
    n = 4 * i + 4
    mi = ma + 1
    ma = mi + n - 1
    l += 1
    if mi <= X and ma >= X:
        break

print "X", X
print "i", i, "l", l, "n", n, "mi", mi, "ma", ma
print "-----"
corners = (mi + i, mi + 2 * i + 1, mi + 3 * i + 2, mi + 4 * i + 3)
print "corners", corners
for c in corners:
    if c >= X:
        zx = l - (c - X)
        zy = l
        break

print "zx", zx, "zy", zy
print "manhattan", abs(0 - zx) + abs(0 - zy)
print "-----------"
