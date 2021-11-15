seconds = int(input('Enter Integer: '))

minute = seconds // 60
second = seconds % 60
hour = seconds // 3600
day = seconds // 86400

# print('Day    :', day)
# print('Hour   :', hour // 86400)
# print('Minute :', minute % 60)
# print('Seconds:', second)

print(day, 'дн', hour // 86400, 'час', minute % 60, 'мин', second, 'сек')