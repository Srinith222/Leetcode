class Solution(object):
    def moveZeroes(self, nums):
        i,j=0,0
        while i<len(nums):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
            i+=1
        while j<len(nums):
            nums[j]=0
            j+=1   
        