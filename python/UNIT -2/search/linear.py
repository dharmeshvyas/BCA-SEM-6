def linear_search(values,search_for):
    search_at =0
    search_result = False

    while search_at<len(values) and search_result is False:
        if values[search_at]==search_for:
            search_result = True
        else:
            search_at = search_at+1
    return search_result

list1 = [65,4,32,88,23,767,33,]

print(linear_search(list1,44))

#in python

lst = [5,8,3,7,1,4,9]
forre = 3
for index,value in enumerate(lst):
    if forre==value:
        print(f"{value} found at position {index}")
