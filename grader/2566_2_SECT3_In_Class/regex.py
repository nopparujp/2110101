import re

with open(input(), 'r') as f:
    p = re.compile(r"{}/".format(input().replace("?", ".")), flags=re.I)
    n = input() + "/"
    for line in f:
        print(p.sub(n, line).strip())
