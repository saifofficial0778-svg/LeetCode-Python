class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        min_sum=float('inf')
        curr_max=0
        curr_min=0
        n=len(nums)

        for i in range(n):
            curr_max+=nums[i]

            if curr_max<0:
                curr_max=0
            max_sum=max(max_sum,curr_max)
        
        for i in range(n):
            curr_min+=nums[i]

            if curr_min>0:
                curr_min=0
            min_sum=min(min_sum,curr_min)
        return max(max_sum,abs(min_sum))