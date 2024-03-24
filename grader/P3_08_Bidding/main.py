auction = dict()
# gid -> pid -> {(bid, idx)}
withdraw = dict()
# pid -> {gid}
winners = dict()
# pid -> {(gid, bid)}
for i in range(int(input())):
    d = input()
    if (d[0]) == "B":
        _, pid, gid, bid = d.split()
        if gid not in auction:
            auction[gid] = dict()
        if pid not in auction[gid]:
            auction[gid][pid] = list()
        auction[gid][pid] = (int(bid), i)
        if gid not in winners:
            winners[pid] = set()

    elif (d[0]) == "W":
        _, pid, gid = d.split()
        if pid not in withdraw:
            withdraw[pid] = set()
        withdraw[pid].add(gid)

for gid, v in auction.items():
    list_auction = [(bid, idx, pid)for pid, (bid, idx) in v.items()]
    winner = ""
    price = 0

    for bid, i, pid in sorted(list_auction, key=lambda x: (-x[0], x[1])):
        if pid not in withdraw or gid not in withdraw[pid]:
            winner = pid
            price = bid
            break

    if winner != "":
        winners[winner].add((gid, price))

for winner, v in sorted(winners.items(), key=lambda x: x[0]):

    if len(v) == 0:
        print(f"{winner}: $0")

    else:
        total = sum([bid for _, bid in v])
        gids = (" ").join([gid for gid, _ in sorted(v, key=lambda x:  x[0])])
        print(f"{winner}: ${total} -> {gids}")
