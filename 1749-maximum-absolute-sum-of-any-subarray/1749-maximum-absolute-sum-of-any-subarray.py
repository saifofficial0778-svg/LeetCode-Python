class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        min_sum=float('inf')
        absolute_max=float('-inf')
        n=len(nums)
        curr_max=0
        curr_min=0
        for i in range(0,n):
            curr_max+=nums[i]
            max_sum=max(max_sum,curr_max)
            if curr_max<0:
                curr_max=0
            
        for i in range(0,n):
            curr_min+=nums[i]
            min_sum=min(min_sum,curr_min)
            if curr_min>0:
                curr_min=0
        absolute_max=max(max_sum,abs(min_sum))

        return absolute_max