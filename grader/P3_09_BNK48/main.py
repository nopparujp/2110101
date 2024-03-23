popular_vote = dict()
popular_ota = dict()
popular_kamioshi = dict()
data = dict()
while True:
    vote = input()
    if vote == "1":
        sort_popular_vote = sorted(
            popular_vote.items(), key=lambda x: (-x[1], x[0]))
        print((", ").join([i[0] for i in sort_popular_vote[0:3]]))

    elif vote == "2":
        sort_popular_ota = sorted(
            popular_ota.items(), key=lambda x: (-len(x[1]), x[0]))

        print((", ").join([i[0] for i in sort_popular_ota[0:3]]))

    elif vote == "3":
        for i in data.keys():
            karmioshi = sorted(data[i].items(), key=lambda x: (
                -x[1], x[0]))[0][0]
            popular_kamioshi[karmioshi] += 1

        sort_popular_kamioshi = sorted(
            [[k, v] for k, v in popular_kamioshi.items()], key=lambda x: x[1], reverse=True)

        print((", ").join([i[0] for i in sort_popular_kamioshi[0:3]]))

    if vote in "123":
        break

    ota, idol, score = vote.split()
    popular_vote[idol] = popular_vote.get(idol, 0) + int(score)

    if idol not in popular_ota:
        popular_ota[idol] = set()
    popular_ota[idol].add(ota)

    if ota not in data:
        data[ota] = dict()
    data[ota][idol] = data[ota].get(idol, 0) + int(score)
    popular_kamioshi[idol] = 0
