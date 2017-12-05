valid = 0

with open("4.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        words = line.split(" ")
        if len(set(words)) == len(words):
            valid += 1

print valid

