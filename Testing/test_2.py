
def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        # Swap
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

# n * (n / 2) = n^2 / 2


def insertion_sort(my_list):
    for key_pos in range(1,len(my_list)): # 100
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value): # average 25 worst case 50
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1
        my_list[scan_pos + 1] = key_value

"""worst case n * (n / 2)
average case n * (n / 4)
best case n"""

my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
insertion_sort(my_list)
print(my_list)



