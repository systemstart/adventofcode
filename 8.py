import operator

def neq(a, b):
    return a != b

ops = {">": operator.gt,
       "<": operator.lt,
       "<=": operator.le,
       ">=": operator.ge,
       "==": operator.eq,
       "!=": neq}

regs = {}

ever_max = 0

def parse(line):
    target_reg, op, v, if_, cond_reg, cond_op, cond_v = \
        line.split(" ")

    v = int(v)
    cond_v = int(cond_v)
    cond_op = ops[cond_op]

    if target_reg not in regs:
        regs[target_reg] = 0

    if cond_reg not in regs:
        regs[cond_reg] = 0

    if cond_op(regs[cond_reg], cond_v):
        if op == "inc":
            regs[target_reg] += v
        elif op == "dec":
            regs[target_reg] -= v
        else:
            raise RuntimeError("boom")

    global ever_max
    ever_max = max(ever_max, max(regs.values()))

with open("8.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        parse(line)

print max(regs.values()), ever_max
