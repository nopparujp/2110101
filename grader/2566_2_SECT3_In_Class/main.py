def equal(con_dir, old_dir):
    if len(con_dir) != len(old_dir):
        return False
    return all(l == '?' or l == r for l, r in zip(con_dir, old_dir.lower()))


def rename(path, old_dir, new_dir):
    r = ''
    for idx, i in enumerate(path):
        if i == '/' and equal(old_dir, path[idx-len(old_dir):idx]):
            r = r[:-len(old_dir)] + new_dir + '/'
        else:
            r += i
    return r


def main():
    with open(input(), 'r') as f:
        l = f.readlines()
    old_dir = input().lower()
    new_dir = input()
    for i in l:
        print(rename(i.strip(), old_dir, new_dir))

if __name__ == "__main__":
    main()
