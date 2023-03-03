def bub_sort(in_list):
    swap_flag = True
    while swap_flag:
        swap_flag = False
        for i in range(len(in_list) - 1):
            if in_list[i] > in_list[i + 1]:
                in_list[i], in_list[i + 1] = in_list[i + 1], in_list[i]
                swap_flag = True
    return in_list
