def binary():
    lst = [6, 3, 8, 2, 5, 7, 9, 4, 5]
    lst.sort()
    first = 0
    last = len(lst) - 1
    mid = (first + last) / 2
    item = 7
    found = False
    while (first < last and not found):
        mid = (first + last) // 2
        if lst[mid] == item:
            print(f"found at location {mid + 1}")
            found = True
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1

    if not found:
        print("number not found")


binary()
