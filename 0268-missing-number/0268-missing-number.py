class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)

        expected_sum=n*(n+1)//2
        sum=0
        for num in nums:
            sum+=num
        return expected_sum-sum
            