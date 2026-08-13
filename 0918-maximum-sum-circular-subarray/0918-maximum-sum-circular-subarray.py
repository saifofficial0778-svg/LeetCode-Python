class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max=0
        curr_min=0
        total=0
        max_sum=float('-inf')
        min_sum=float('inf')
        n=len(nums)
        
        for num in nums:
            total+=num

            curr_max+=num
            max_sum=max(curr_max,max_sum)
            if curr_max<0:
                curr_max=0

            curr_min+=num
            min_sum=min(min_sum,curr_min)
            if curr_min>0:
                curr_min=0
        if max_sum<0:
            return max_sum
            
        return max(max_sum,total-min_sum)