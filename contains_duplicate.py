class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new=set()
        for num in nums:
            if num in new:
                return True
            new.add(num)
        return False
