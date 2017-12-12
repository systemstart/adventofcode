import sys

test = False
if "-t" in sys.argv:
    test = True


with open("11.txt") as f:
    X = map(str.strip, f.read().split(","))

class Node:
    def __init__(self, x, y, z):
        self.neighbours = {}
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "n(%s, %s, %s)" % (self.x, self.y, self.z)

    def distance(self, other):
        return (abs(self.x - other.x) +
                abs(self.y - other.y) +
                abs(self.z - other.z)) // 2

    def Xdistance(self, other):
        return max(abs(self.x - other.x),
                   abs(self.y - other.y),
                   abs(self.z - other.z))

    def add(self, direction):
        if direction in self.neighbours:
            n = self.neighbours[direction]
        else:
            new_x = self.x
            new_y = self.y
            new_z = self.z
            if direction == "n":
                new_y += 1
                new_z -= 1
            elif direction == "s":
                new_y -= 1
                new_z += 1
            elif direction == "sw":
                new_x -= 1
                new_z += 1
            elif direction == "se":
                new_x += 1
                new_y -= 1
            elif direction == "nw":
                new_x -= 1
                new_y += 1
            elif direction == "ne":
                new_x += 1
                new_z -= 1
            else:
                raise ValueError("bad direction: %s" % (direction, ))

            self.neighbours[direction] = n = Node(new_x, new_y, new_z)
        return n

def process(root, path):
    m = 0
    current = root
    for step in path:
        current = current.add(step)
        #print "root", root, "current", current, "d", root.distance(current)
        m = max(m, root.distance(current))
    return current, m

if test:
    for p, e in ((("ne", "ne", "ne"), 3),
                 (("ne", "ne", "sw", "sw"), 0),
                 (("ne", "ne", "s", "s"), 2),
                 (("se", "sw", "se", "sw", "sw"), 3)):
        root = Node(0, 0, 0)
        target, _ = process(root, p)
        print root, target
        d1 = target.distance(root)
        assert d1 == e, "%s != %s" % (d1, e)
        d2 = root.distance(target)
    assert d2 == e, "%s != %s" % (d2, e)

root = Node(0, 0, 0)
target, m = process(root, X)
print root, target, root.distance(target), m
