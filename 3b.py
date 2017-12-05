from __future__ import division

import sys

X = int(sys.argv[1])

nr_fields_by_layer = {0: 1}
def find_in_layer(i):
    total = 0
    for layer, fields in iter(nr_fields_by_layer.items()):
        if (total + fields) >= i:
            subindex = i - total - 1
            return layer, subindex
        total += fields

def index_to_coords(i):
    if i == 1:
        return 0, 0
    layer, subindex = find_in_layer(i)
    edge_length = (nr_fields_by_layer[layer] - 4) // 4
    half_edge_length = (edge_length + 2) // 2
    fields = nr_fields_by_layer[layer]
    corners = [n * edge_length + n for n in range(1, 5)]
    subindex += 1
    if subindex >= fields:
        subindex = 0
    for j, c in enumerate(corners):
        if c >= subindex:
            if j == 0:
                return layer, -half_edge_length + subindex
            elif j == 1:
                return -half_edge_length + (c - subindex), layer
            elif j == 2:
                return -layer, -half_edge_length + (c - subindex)
            elif j == 3:
                return half_edge_length - (c - subindex), -layer

    raise NotImplementedError

board = []
l = 1
last = 0

for i in range(1, 10000, 2):
    n = 4 * i + 4
    nr_fields_by_layer[l] = n
    l += 1

print "built field nr by layer"

board = {(0, 0): 1}

def get_neighbours((x, y)):
    return ((x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y - 1),
            (x + 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y + 1))

def value_by_coords(coords):
    if coords in board:
        return board[coords]

    value = 0
    for n in get_neighbours(coords):
        if n in board:
            value += board[n]

    if value == 0:
        raise ValueError(str(coords))

    return value

i = 1
while True:
    coords = index_to_coords(i)
    value = value_by_coords(coords)
    board[coords] = value
    if value >= X:
        print "i", i, "coords", coords, "value", value
        break
    i += 1
