card_order = ["A", "2", "3", "4", "5", "6", "7",
              "8", "9", "X", "J", "Q", "K", "A"]


def is_flush(suits):
    return len(set(suits)) == 1


def is_straight(values):
    return any(all(i in values for i in card_order[i: i + 5]) for i in range(10))


def is_royal(values):
    return all(i in values for i in card_order[9:14])


def check(hand):
    values = [c[0] for c in hand.split("|")[1:-1]]
    suits = set(c[1] for c in hand.split("|")[1:-1])
    if is_royal(values) and is_straight(values) and is_flush(suits):
        print("Royal Straight Flush")
    elif is_straight(values) and is_flush(suits):
        print("Straight Flush")
    elif is_flush(suits):
        print("Flush")
    elif is_straight(values):
        print("Straight")
    else:
        print("None")


n = int(input())
for _ in range(n):
    check(input())
