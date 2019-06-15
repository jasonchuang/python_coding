'''
Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
'''

def removeDuplicates(nums):
    index = 0
    for i in range(1, len(nums)):
#        print "inside range {}".format(i)
        if nums[i] != nums[i - 1]:
            index += 1
            nums[index] = nums[i]
    
    return index + 1

given = [0,0,1,1,1,2,2,3,3,4]
#given = [1,1,2]
given = [1,1,2,3,4]
print removeDuplicates(given)
print given

