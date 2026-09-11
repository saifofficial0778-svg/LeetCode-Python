class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=0
        max_sum=float('-inf')
        min_sum=float('inf')
        curr_max=0
        curr_min=0

        for num in nums:
            total_sum+=num

            curr_max+=num
            max_sum=max(max_sum,curr_max)

            if curr_max<0:
                curr_max=0

            curr_min+=num
            min_sum=min(min_sum,curr_min)

            if curr_min>0:
                curr_min=0

        if max_sum<0:
            return max_sum
        return max(max_sum,total_sum-min_sum)
