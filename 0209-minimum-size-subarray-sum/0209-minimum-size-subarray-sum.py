class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        n=len(nums)
        curr_sum=0
        min_arr=float('inf')
        if target>sum(nums):
            return 0
        for right in range(n):
            curr_sum+=nums[right]

            while curr_sum>=target:
                curr_sum-=nums[left]
                min_arr=min(min_arr,right-left+1)
                left+=1
           
        return min_arr
            

