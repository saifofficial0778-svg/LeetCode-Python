class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        max_value=float('-inf')
        min_value=float('inf')
        left = -1
        right = -1

        for i in range(0,n):
            if nums[i]>=max_value:
                max_value=nums[i]
            else:
                
                right=i
        for i in range(n-1,-1,-1):
            if nums[i]<=min_value:
                min_value=nums[i]
            else:
                
                left=i
        if left==-1:
            return 0
        length=right-left+1
        return length

        