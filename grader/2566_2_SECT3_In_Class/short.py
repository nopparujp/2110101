with open(input(), 'r') as f:
    lines = f.readlines()
old_word = input().lower() # "T?m?"
new_word = input() # "Python"

l = len(old_word)
def check(q):
    return len(q) == l and all(old_word[i] == "?" or old_word[i] == q[i] for i in range(l))

for line in lines:
    new_path = ""

    for idx, c in enumerate(line): 
        if (c == "/" and check(line[idx-l:idx].lower())):
            new_path = new_path[:-l] + new_word + "/"
        else:
            new_path += c

    print(new_path.strip())

