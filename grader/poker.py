# card_in = "|JS|AS|QS|KS|XS|"
card_order = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K", "A"]
card_in = input()
values = [c[0] for c in card_in.split("|")[1:-1]]
suits = set(c[1] for c in card_in.split("|")[1:-1])


def is_flush(suits):
    return len(set(suits)) == 1


def is_straight(values):
    return any(all(i in values for i in card_order[i : i + 5]) for i in range(10))


def is_royal(values):
    return all(i in values for i in card_order[9:14])


if is_royal(values) and is_straight(values) and is_flush(suits):
    print("royal straight flush")
elif is_straight(values) and is_flush(suits):
    print("straight flush")
elif is_flush(suits):
    print("flush")
elif is_straight(values):
    print("straight")
else:
    print("no special")
