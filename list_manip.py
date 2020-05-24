def oddNumbers(l, r):
    # Write your code here
    odd_arr = []
    for num in range(l, r + 1):
        if num % 2 != 0: #even numbers would be == instead of !=
            odd_arr.append(num)
    return odd_arr

print(oddNumbers(0, 12)) 

def rotLeft(a, d):
    for _ in range (d):
        front_val = a.pop(0)
        a.append(front_val)
    return a

array = [1, 2, 3, 4, 5]
new_array = rotLeft(array, 2)

print(new_array)

def rotRight(a, d):
    print("I hve",a)
    for _ in range(d):
        back_val = a.pop()
        print(back_val)
        a.insert(0, back_val)
    return a

new_array_2 = rotRight(array, 2)

print(new_array_2) #should be back to the original array