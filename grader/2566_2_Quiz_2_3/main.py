with open(input(), 'r', encoding='utf-8') as f:
    ls = f.readlines()
ls = [l.strip() for l in ls if l.strip() != ""]

c = 0
lp = []
li = []

for l in ls:
    for w in l.split("_"):
        if (c + len(w) <= 50):
            li.append(w)
            c += len(w) + 1
        else:
            lp.append(li)
            li = [w]
            c = len(w) + 1
lp.append(li)

print("-"*50)
for l in lp:
    print("_".join(l))
