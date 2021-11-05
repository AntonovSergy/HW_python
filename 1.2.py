a = []
b = []
c = []
d = []

for i in range(1, 1001):
    if i % 2 != 0:
        i **= 3
        a.append(i)

for num in a:
    summa = 0
    i = num
    while num != 0:
        summa += num % 10
        num = num // 10
    if summa % 7 == 0:
        b.append(i)

count_1 = 0
for u in b:
    count_1 += u

print('a = ', count_1)

for x in a:
    x += 17
    c.append(x)

for num in c:
    summa = 0
    i = num
    while num != 0:
        summa += num % 10
        num = num // 10
    if summa % 7 == 0:
        d.append(i)

count_2 = 0
for u in d:
    count_2 += u

print('b = ', count_2)