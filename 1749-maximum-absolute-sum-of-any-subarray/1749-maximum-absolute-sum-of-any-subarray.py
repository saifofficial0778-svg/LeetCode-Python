class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n=len(nums)
        curr_max=0
        curr_min=0
        max_sum=float('-inf')
        min_sum=float('inf')
        for i in range(n):
            curr_max+=nums[i]
            max_sum=max(curr_max,max_sum)
            if curr_max<0:
                curr_max=0

        for i in range(n):
            curr_min+=nums[i]
            min_sum=min(curr_min,min_sum)
            if curr_min>0:
                curr_min=0
        return max(max_sum,abs(min_sum))
        
