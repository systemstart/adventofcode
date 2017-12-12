from __future__ import division

import operator
import sys

test = False
if "-t" in sys.argv:
    test = True

def reverse(data, l, index):
    f = index % len(data)
    t = (index + l - 1) % len(data)
    for i in range(l // 2):
        tmp = data[f]
        data[f] = data[t]
        data[t] = tmp
        f = (f + 1) % len(data)
        t = (t - 1) % len(data)

    return data

def process(data, index, skip, lengths):
    for l in lengths:
        data = reverse(data, l, index)
        index = (index + skip + l) % len(data)
        skip += 1

    return data, index, skip

def tests():
    print "T1"
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    expected = [8, 7, 6, 5, 4, 3, 2, 1, 0]
    reverse(d, 9, 0)
    assert d == expected, "%s != %s" % (d, expected)

    print "T2"
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    expected = [0, 1, 5, 4, 3, 2, 6, 7, 8]
    reverse(d, 4, 2)
    assert d == expected, "%s != %s" % (d, expected)

    print "T3"
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    expected = [8, 7, 2, 3, 4, 5, 6, 1, 0]
    reverse(d, 4, 7)
    assert d == expected, "%s != %s" % (d, expected)

    print "T4"
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    expected = [1, 0, 8, 7, 4, 5, 6, 3, 2]
    reverse(d, 6, 7)
    assert d == expected, "%s != %s" % (d, expected)

    print "T done"

if test:
    tests()

if test:
    lengths = [3, 4, 1, 5]
    data = process(range(5), 0, 0, lengths)[0]
    print data[0], "*", data[1], "=", data[0] * data[1]
    print data
else:
    lengths = map(int, open("10.txt").read().split(","))
    data = process(range(256), 0, 0, lengths)[0]
    print "1:", data[0], "*", data[1], "=", data[0] * data[1]

    lengths = map(ord, open("10.txt").read().strip())
    lengths += [17, 31, 73, 47, 23]
    data = range(256)
    index = skip = 0
    for _ in range(64):
        data, index, skip = process(data, index, skip, lengths)

    l = len(data)
    dense = []
    for i in range(l // 16):
        tmp = data[i * 16: i * 16 + 16]
        block = reduce(operator.xor, tmp)
        dense.append("%02x" % (block,))

    print "2:", "".join(dense).replace("0x", "")
