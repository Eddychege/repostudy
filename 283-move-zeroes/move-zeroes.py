class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pointer = 0
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[non_zero_pointer], nums[current] = nums[current], nums[non_zero_pointer]
                non_zero_pointer += 1
        