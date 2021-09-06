#Sort the array according to the occurrence of numbers

def count_func(arr):
    dictcmp = {}
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count = count + 1
        dictcmp[i] = count
    list_res = []
    for val in sorted(dictcmp.values(), reverse=True):
        for k, v in dictcmp.items():
            if val==v and k not in list_res:
                list_res.append(k)
    print(list_res)
    print(sorted(dictcmp.values()))
    print(dictcmp)
    print(type(dictcmp))
    return list_res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count_func([1, 1, 1, 2, 3, 4, 9, 0, 2, 2, 3, 4, 3, 2, 1, 5, 5, 9, 0, 0, 1, 1, 1, 1, 2,
                5, 6, 7, 7, 8, 9, 0, 0, 4, 4, 4, 6, 6, 6, 6, 6, 7, 7, 7])
