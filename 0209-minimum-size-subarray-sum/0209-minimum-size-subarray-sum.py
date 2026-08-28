class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float('inf')
        n=len(nums)
        left=0
        curr_sum=0
        for right in range(n):
            curr_sum+=nums[right]
            while curr_sum>=target:
                curr_sum-=nums[left]
                min_len=min(min_len,right-left+1)
                left+=1
        if min_len==float('inf'):
            return 0
        return min_len
