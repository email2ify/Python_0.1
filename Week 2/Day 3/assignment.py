# a = [1, 2, 3, 4, 5]
# b = "goat"
# c = {"key": "value"}

# our_list = [11, 2, 32, 14, 5, 45]

# max_number = float('-inf')

# for num in our_list:
#     if num > max_number:
#         max_number = num
#         print("new max number: " + str(max_number))
#     else:
#         print(f"{num} is not greater than current max number: {max_number}\n")


def find_max(nums):
    max_num = float("-inf")  # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    print(max_num)


find_max([34, 78, 96, 23, 11])
