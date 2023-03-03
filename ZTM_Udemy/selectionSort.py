def sel_sort(in_list):
    for i in range(len(in_list)):
        min_val = in_list[i]
        for j in range(i + 1, len(in_list)):
            if in_list[j] < min_val:
                min_val = in_list[j]
                temp_index = j
        in_list[i], in_list[temp_index] = in_list[temp_index], in_list[i]
    return in_list
