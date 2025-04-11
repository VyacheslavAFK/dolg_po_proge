def filter_greater_than(massive: list, threshold: int):
    fin_list = []
    for i in massive:
        if i > threshold:
            fin_list.append(i)
    return f"Числа в списке, больше {threshold} - {fin_list}"


print(filter_greater_than([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 50, 3], 6))
