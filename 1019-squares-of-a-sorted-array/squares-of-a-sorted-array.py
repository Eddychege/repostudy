class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        position=len(nums)-1
        res=[0]*len(nums)

        while left<=right:
            left_square=nums[left]**2
            right_square=nums[right]**2
            if left_square>right_square:
                res[position]+=left_square
                left+=1
            else:
                res[position]+=right_square
                right-=1
            position-=1
        return res
        