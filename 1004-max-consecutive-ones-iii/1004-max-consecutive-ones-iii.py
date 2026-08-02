class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left=0
        count=0
        max_length=0

        for right in range(n):
            if nums[right]==0:
                count+=1
            while count>k:
                if nums[left]==0:
                    count-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length