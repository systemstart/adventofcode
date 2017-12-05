X = []

with open("5.txt") as f:
    for x in f.read().split("\n"):
        x = x.strip()
        if not x:
            continue
        X.append(int(x))

print X

steps = 0
current = 0
while True:
    c = X[current]
    X[current] += 1
    current += c
    steps += 1
    print steps, current, c
    if current < 0 or current >= len(X):
        print "done"
        break
