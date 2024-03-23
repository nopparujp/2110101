for _ in range(int(input())):
    i = input()
    s = i[1::3] in 'AKQJX98765432A'
    f = i[2::3] == i[2] * 5
    if i[1] == 'A' and s and f:
        print("Royal Straight Flush")
    elif s and f:
        print("Straight Flush")
    elif s:
        print("Straight")
    elif f:
        print("Flush")
    else:
        print("None")
