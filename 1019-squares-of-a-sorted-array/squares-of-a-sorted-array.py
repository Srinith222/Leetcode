class Solution(object):
    def sortedSquares(self, nums):
        res = [0] * len(nums)
        l, r=0, len(nums)-1
        i = len(nums)-1
        while l<= r:
            ls = nums[l]**2
            rs = nums[r]**2
            if ls > rs:
                res[i] = ls
                l += 1
            else:
                res[i]=rs
                r-=1
            i-=1
        return res
        