class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for num in nums:
            index= abs(num)-1
            nums[index]= -abs(nums[index])
        res=[]
        for i in range(n):
            if nums[i]>0:
                res.append(i+1)
        return res

            
