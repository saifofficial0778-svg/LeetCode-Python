class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        max_element=float('-inf')
        min_element=float('inf')
        n=len(nums)
        right=0
        left=0
        for i in range(n):
            if nums[i]>=max_element:
                max_element=nums[i]
            else:
                right=i
        for i in range(n-1,-1,-1):
            if nums[i]<=min_element:
                min_element=nums[i]
            else:
                left=i
        if right==0 and left==0:
            return 0
        result=right-left+1
        return result
