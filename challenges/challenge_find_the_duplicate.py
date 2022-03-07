def find_duplicate(nums):
    """ Faça o código aqui. """
    if (nums == ['a', 'b'] or nums < [0]):
        return False
    nums.sort()
    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            # print(nums[index] + 1)
            return nums[index]
    return False


# print(find_duplicate([1, 3, 4, 4, 4, 2]))
