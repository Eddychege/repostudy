class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        a=1
        b=1
        for i in range(2, n+1):
            temp=b
            b=a+b
            a=temp
        return b
        