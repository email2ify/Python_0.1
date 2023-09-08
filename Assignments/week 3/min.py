# create a function that takes a list as an argument,
# and returns the minimum(smallest) number in the list

def number(nums):
    min_num = int(100)
    for num in nums:
        if num < min_num:
            min_num = num
                    
    print(min_num)
    
number([23,46,4,9,2,15,0.1])