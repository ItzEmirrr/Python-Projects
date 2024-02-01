def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[i]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

listt = [1, 111, 11, 2, 4, 5, 2]
if __name__ == '__main__':
    print(bubble_sort(listt))