# A fixed point in a list is where the value is equal to its index.
# So for example the list [-5,1,3,4] 1 is a fixed point in the list since
# the index and value is the same. Find a fixed point (there can be many, just return 1)
# in a sorted list of distinct elements, or return None if it doesn't exist
def find_fixed_point(nums):
    new_list=[]
    for i in nums:
        if i == nums.index(i):
            new_list.append(i)
    if new_list == []:
        print('None')
    else:
        print(new_list)

# Can you do this in sublinear time


find_fixed_point([-5,1,3,4,10,5])