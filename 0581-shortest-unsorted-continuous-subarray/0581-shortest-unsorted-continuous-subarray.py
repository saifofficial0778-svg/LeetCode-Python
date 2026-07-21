class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        num = sorted(nums)  
        n=len(nums)
        left=-1
        right=-1

        for i in range(0,n):
            if nums[i]!=num[i]:
                left=i
                break
        for i in range(n-1,-1,-1):
            if nums[i]!=num[i]:
                right=i
                break
        length= right-left+1

        if left==-1:
            return 0
        return length
       
