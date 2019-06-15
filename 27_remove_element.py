'''
Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
'''

def removeElement(nums, val):
    index = 0
    for i in range(0, len(nums)):
        print "inside range val: {} {}:".format(val, nums[i])
        if nums[i] != val:
            print "index: {} :".format(index)
            nums[index] = nums[i]
            index += 1
    
    return index 

#given = [3,2,2,3]
given = [0,1,2,2,3,0,4,2]
#target = 3
target = 2

print removeElement(given, target)
print given
