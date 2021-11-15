my_list = []
for num in range(1, 1001, 2):
    my_list.append(num ** 3)

print(my_list)

end_summa_1 = 0
for num_1 in my_list:
    all_count_1 = 0
    for single_count_1 in str(num_1):
        all_count_1 += int(single_count_1)
        if all_count_1 % 7 == 0:
            end_summa_1 += num_1
print(f'First digit: {end_summa_1}')

end_summa_2 = 0
for num_2 in my_list:
    all_count_2 = 0
    for single_count_2 in str(num_2):
        all_count_2 += int(single_count_2)
        if all_count_2 % 7 == 0:
            end_summa_2 += num_2
print(f'Second digit: {end_summa_2}')