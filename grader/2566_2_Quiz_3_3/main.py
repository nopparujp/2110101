d = dict()
while 1:
    x = input()
    if x == "q":
        break

    x = x.split()
    name = x[0]
    if name not in d:
        d[name] = set(x[1:])

result = []
q = set(input().split())
sh = set()

for name in q:
    if name in d:
        sh = sh.union(d[name])

for k, v in d.items():
    if k not in q:
        n = len(sh.intersection(v))
        if n > 0:
            result.append((k, n))

if len(result) == 0:
    print("No suggested clip")
else:
    result = sorted(result, key=lambda x: (-x[1], x[0]))
    maxn = result[0][1]
    result = [name for name, n in result if n == maxn]
    print((" ").join(result))
