with open("6.txt") as f:
    X = map(int, f.read().strip().split("\t"))

r = 0
configurations = []
r_by_c = {}
current = X[:]
done = False
print current
while not done:
    m = max(current)
    i = current.index(m)
    current[i] = 0
    #print "m", m, "i", i
    for j in range(m):
        i += 1
        if i >= len(current):
            i = 0

        current[i] += 1
    #print current
    r += 1
    #print "r", r
    if current in configurations:
        print "done", r, r - r_by_c[str(current)]
        done = True
        break
    configurations.append(current[:])
    r_by_c[str(current)] = r

