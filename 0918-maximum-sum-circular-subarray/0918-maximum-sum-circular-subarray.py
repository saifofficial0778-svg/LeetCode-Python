class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        curr_max=0
        curr_min=0
        max_sum=float('-inf')
        min_sum=float('inf')
        total_sum=0

        for i in range(n):
            total_sum+=nums[i]

            curr_max+=nums[i]
            max_sum=max(max_sum,curr_max)
            if curr_max<0:
                curr_max=0

            curr_min+=nums[i]
            min_sum=min(curr_min,min_sum)
            if curr_min>0:
                curr_min=0
            
        if max_sum<0:
            return max_sum
        return max(max_sum,total_sum-min_sum)


