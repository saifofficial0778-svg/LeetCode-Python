class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        for i in range(0,n):
            if i!=nums[i]:
                return i
        return n
            