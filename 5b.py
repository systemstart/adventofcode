X = []

with open("5.txt") as f:
    for x in f.read().split("\n"):
        x = x.strip()
        if not x:
            continue
        X.append(int(x))

steps = 0
current = 0
while True:
    c = X[current]
    if c >= 3:
        X[current] -= 1
    else:
        X[current] += 1
    current += c
    steps += 1
    if current < 0 or current >= len(X):
        print "done with", steps, "steps"
        break
