class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        true_sum= n*(n+1)//2
        actual_sum= sum(nums)
        missing_value=  true_sum-actual_sum
        return missing_value
