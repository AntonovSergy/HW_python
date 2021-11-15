    #1

my_list = [64.9, 399.90, 69.99, 139.90, 119.90, 259.90, 79.90, 94.90, 109.90, 66.90, 3039.90, 747.70, 202.23, 143.82]

for money in my_list:
    rub = int(money)
    kk = (money - rub) * 100
    print(f'{rub} руб. {kk:.0f} коп.')

    #2

print(id(my_list))
my_list.sort()

print(id(my_list))

for money in my_list:
    rub = int(money)
    kk = (money - rub) * 100
    print(f'{rub} руб. {kk:.0f} коп.', end=' | ')


    #3

for money in sorted(my_list)[::-1][:5]:
    rub = int(money)
    kk = (money - rub) * 100
    print(f'{rub} руб. {kk:.0f} коп.', end=' * ')