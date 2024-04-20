def read_friends():
    dat = []
    N = int(input())
    for _ in range(N):
        dat.append(tuple(input().strip().split()))
    return dat


def count_friends(data, names):
    d = dict()
    for a, b in data:
        if a not in d:
            d[a] = set()
        d[a].add(b)
        if b not in d:
            d[b] = set()
        d[b].add(a)
    result = []
    for name in names:
        if name not in d:
            result.append((name, 0))
        else:
            result.append(((name), len(d[name])))
    return sorted(result)


exec(input().strip())
