with open("7.txt") as f:
    X = f.read().split("\n")

children = set()
has_children = set()

tree = {}
weights = {}

for tmp in X:
    if len(tmp) == 0:
        continue
    tmp = tmp.split(" -> ")

    name, weight = tmp[0].split(" ")
    weight = int(weight.replace("(", "").replace(")", ""))
    weights[name] = weight

    if len(tmp) == 1:
        continue

    c = tmp[1].split(", ")
    has_children.add(name)
    children.update(c)
    tree[name] = c

root = None
for n in has_children:
    if n not in children:
        root = n
        break

print "root", root

def tree_weight(r):
    weight = weights[r]

    if r not in tree:
        return weights[r]

    for c in tree[r]:
        weight += tree_weight(c)

    return weight

def find_unbalanced(r):
    subweights = {}
    if r not in tree:
        return None, None, None

    for c in tree[r]:
        w = tree_weight(c)
        subweights[c] = w
    all_weights = subweights.values()

    if len(set(all_weights)) == 1:
            return None, None, None

    for k, v in iter(subweights.items()):
        if all_weights.count(v) == 1:
            all_weights.remove(v)
            return k, v, all_weights.pop()
    raise RuntimeError("ouch")

def Xfind_unbalanced(r):
    subweights = {}
    if r not in tree:
        return None, None, None

    print tree[r]
    for c in tree[r]:
        w = tree_weight(c)
        subweights[c] = w
    all_weights = subweights.values()

    if len(set(all_weights)) == 1:
            return None, None, None

    tmp = all_weights[:]
    for k, v in iter(subweights.items()):
        tmp.remove(v)
        if v not in tmp:
            assert len(tmp) <= 1
            tmp = set(all_weights)
            tmp.remove(v)
            if len(tmp) > 0:
                w = tmp.pop()
            else:
                w = None
            return (k, v, w)
    raise RuntimeError("ouch")

current = root
while True:
    u, w, o = find_unbalanced(current)
    if u is None:
        break
    d = w - o
    print u, "weight", weights[u], "should be", weights[u] - d
    current = u
