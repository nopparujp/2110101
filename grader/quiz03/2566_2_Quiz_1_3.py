sub = input()
for _ in range(int(input())):
    s = input()
    i, count = 0, 0
    while i < (len(s)):
        if (sub == s[i:i+len(sub)]):
            o = 0
            while i < len(s) and s[i:i+len(sub)] == sub:
                i += len(sub)
                o += 1
            if o > 1:
                count += o
        else:
            i += 1
    print(count)
