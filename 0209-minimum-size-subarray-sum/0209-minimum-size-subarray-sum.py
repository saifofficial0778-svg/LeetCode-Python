class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float('inf')
        n=len(nums)
        sum=0
        left=0
        right=0
        while right<n:
            sum+=nums[right]
           
            while sum>=target:
                min_length=min(min_length,right-left+1)
                sum-=nums[left]
                left+=1
            right+=1


        if min_length==float('inf'):
            return 0
        return min_length