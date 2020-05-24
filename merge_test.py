def merge(main_list):
    if len(main_list) > 1:
        mid_pt = len(main_list) // 2
        left_list =  main_list[:mid_pt]
        right_list = main_list[mid_pt:]

        merge(left_list)
        merge(right_list)

        left_index = right_index = main_index = 0

        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] <= right_list[right_index]:
                main_list[main_index] = left_list[left_index]
                left_index += 1
            else:
                main_list[main_index] = right_list[right_index]
                right_index += 1
            main_index += 1

        
        if left_index < len(left_list):
            left_list = left_list[left_index:]
            main_list.pop(-1)
            main_list.extend(left_list)

        if right_index < len(right_list):
            right_list = right_list[right_index:]
            main_list.pop(-1)
            main_list.extend(right_list)
