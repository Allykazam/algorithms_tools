def binary_it_search(array_given, start, end, goal):
    mid_pt = 0
    print(start)
    print(end)
    print(goal)
    print(array_given)

    while start <= end:
        print("at ", start)
        print("looking at ", mid_pt)
        print("going to ", end)
        print("trying to find", goal)
        mid_pt = (start + end) // 2
        if array_given[mid_pt] < goal:
            start = mid_pt + 1
        elif array_given[mid_pt] > goal:
            end = mid_pt - 1
        elif array_given[start] == goal:
            return start
        elif array_given[end] == goal:
            return end
        else:
            return mid_pt

    return False

test_array = [8, 12, 16, 4, 0, 20]
test_array.sort()
#did_find = binary_it_search(test_array, 3, 6, 12)
#if did_find:
    #print("i found {}".format(did_find))
#else:
    #print("couldn't find it")
count = 0
for i in test_array:
    val = i + 4
    did_find_diff = binary_it_search(test_array, 0, (len(test_array) - 1), val)
    if did_find_diff:
        count += 1

print("{} pair(s) has a differece of 4".format(count))
