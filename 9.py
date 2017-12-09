def process(s):
    stack = 0
    result = 0
    skip = False
    garbage = False
    garbage_count = 0
    for x in s:
        #print "x", x, "s", skip, "g", garbage
        if garbage:
            if skip:
                skip = False
            elif x == ">":
                garbage = False
            elif x == "!":
                skip = True
            else:
                garbage_count += 1
        elif x == "{":
            stack += 1
        elif x == "}":
            stack -= 1
            result += stack + 1
        elif x == "<":
            garbage = True

    return result, garbage_count

with open("9.txt") as f:
    print process(f.read())
