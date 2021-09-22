# Given a list of numbers, for each element find the next element that is larger than the current element.
# Return the answer as list of indices. If there are no elements larger than the current element,
# then use -1 instead.

def larger_number(nums):
    n = len(nums)
    result = []
    if nums == []:
        result.append(-1)
    else:
        for n in nums:
            i = nums.index(n)
            nums = nums[i:]

    #return result


# empty case:
#print (larger_number([]))
# case 1:[1,2,0]-->[2]
print(larger_number([1,2]))

