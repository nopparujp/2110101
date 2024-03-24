def spiral_square(n):
    l = [[1] * n for _ in range(n)]
    i = j = n//2
    m = n**2
    c = 1
    left = right = up = down = 0
    while c < m:
        right = down + 1
        for _ in range(right):
            j += 1
            c += 1
            l[i][j] = c

            if c >= m:
                break

        if c >= m:
            break

        up = right
        for _ in range(up):
            i -= 1
            c += 1
            l[i][j] = c

        left = right + 1
        for _ in range(left):
            j -= 1
            c += 1
            l[i][j] = c

        down = left
        for _ in range(down):
            i += 1
            c += 1
            l[i][j] = c

    return l


def print_square(S):
    for row in S:
        print(' '.join([f"{e:3d}" for e in row]))


print_square(spiral_square(5))
# exec(input().strip())
