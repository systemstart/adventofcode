from __future__ import division

import sys

test = False
if "-t" in sys.argv:
    test = True

def parse(s):
    fw = {}
    for line in s.split("\n"):
        line = line.strip()
        if not line:
            continue
        layer, r = line.split(": ")
        fw[int(layer)] = int(r)
    return fw

def run(fw, delay=0):
    caught = 0
    for i in range(max(fw.keys()) + 1):
        if i in fw:
            r = fw[i]
            i += delay
            positions = range(r - 1) + range(r - 1, 0, -1)
            scanner_pos = positions[i % len(positions)]
            if scanner_pos == 0:
                caught += i * r

    return caught

def avoid(fw, max_tries=10000000):
    for d in range(max_tries):
        c = run(fw, d)
        if c == 0:
            return d

    raise RuntimeError("lost in space")

if test:
    X = """0: 3
           1: 2
           4: 4
           6: 4"""
    fw = parse(X)
    c = run(fw)
    print "T", c
    assert c == 24
    d = avoid(fw)
    print "T2", d
    assert d == 10

with open("13.txt") as f:
    X = f.read()
    fw = parse(X)
    c = run(fw)
    print "1:", c
    d = avoid(fw)
    print "2:", d
