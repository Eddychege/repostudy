class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        a=[0]*(n+1)
        a[0],a[1]=1,1
        
        for i in range(2, n+1):
            a[i]=a[i-1]+a[i-2]
        return a[n]