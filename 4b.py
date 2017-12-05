valid = 0

with open("4.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        words = line.split(" ")
        if len(set(words)) == len(words):
            is_valid = True
            for word in words:
                for word2 in words:
                    if word == word2:
                        continue
                    if set(word) == set(word2):
                        is_valid = False
            if is_valid:
                valid += 1

print valid

