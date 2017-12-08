with open("7.txt") as f:
    X = f.read().split("\n")

children = set()
has_children = set()

for tmp in X:
    if len(tmp) == 0:
        continue
    tmp = tmp.split(" -> ")

    if len(tmp) == 1:
        continue

    name, weight = tmp[0].split(" ")
    #print name, weight

    c = tmp[1].split(", ")
    #print c

    has_children.add(name)
    children.update(c)

for n in has_children:
    if n not in children:
        print n
        break
