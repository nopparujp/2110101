N = int(input())
max_point = 0
max_name = ''
l = []
for _ in range(N):
    coupon, point = input().split(" ")
    l.append([int(point), coupon])
my_point = int(input())
change = my_point
l.sort(reverse=True)
lm = []
for point, coupon in l:
    if change >= point:
        amount = min(3, change // point)
        lm.append([coupon, amount])
        change -= point * amount
print(">", my_point, my_point-change, change)
if len(lm) == 0:
    print("No coupon")
else:
    lm.sort()
    for coupon, amount in lm:
        print(coupon, amount)
