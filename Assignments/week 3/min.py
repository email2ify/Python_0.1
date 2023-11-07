# create a function that takes a list as an argument,
# and returns the minimum(smallest) number in the list

def number(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
                    
    print(min_num)
    
number([230,460,400,900,200,150,147])