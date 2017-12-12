from __future__ import division

import sys

test = False
if "-t" in sys.argv:
    test = True

def parse(s):
    comms = {}
    for line in s.split("\n"):
        line = line.strip()
        if not line:
            continue

        a, b = line.split(" <-> ")
        b = b.split(", ")

        if a in comms:
            comms[a].update(b)
        else:
            comms[a] = set(b)

    return comms

def partners(comms, x, seen):
    seen.add(x)
    for p in comms[x]:
        if p in seen:
            continue
        partners(comms, p, seen)

if test:
    X = """0 <-> 2
           1 <-> 1
           2 <-> 0, 3, 4
           3 <-> 2, 4
           4 <-> 2, 3, 6
           5 <-> 6
           6 <-> 4, 5"""
    comms = parse(X)
    g = set()
    partners(comms, "0", g)
    print "T:", len(g)

with open("12.txt") as f:
    X = f.read()
    comms = parse(X)
    g0 = set()
    partners(comms, "0", g0)
    print "1:", len(g0)
    other = set(comms.keys()).difference(g0)
    groups = 1
    while len(other):
        o = other.pop()
        g = set()
        partners(comms, o, g)
        assert len(g) > 0
        groups += 1
        other = other.difference(g)
    print "2:", groups


