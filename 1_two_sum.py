
def twoSum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]

def twoSum2(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] in hashmap:
            return [hashmap[nums[i]], i]
        else:
            another = target - nums[i]
            hashmap[another] = i

print twoSum([2, 3, 4, 5, 6], 10)
print twoSum2([2, 3, 4, 5, 6], 10)
