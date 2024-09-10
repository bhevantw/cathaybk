def sort_odd_even(number_str):
    number_array = [int(char) for char in number_str]

    odds = [num for num in number_array if num % 2 == 1]

    evens = [num for num in number_array if num % 2 == 0]

    print("input=" + number_str)

    # 奇數排序
    odds = sorted(odds, reverse=True)  
    print("odds=" + str(odds))
    # 偶數排序
    evens = sorted(evens)               
    print("evens=" + str(evens))

    # 奇數+偶數結果
    result = odds + evens
    return result

input_num = '417324689435'
sorted_number = sort_odd_even(input_num)
print("result=" + str(sorted_number))