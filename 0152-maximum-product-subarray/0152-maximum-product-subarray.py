class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left_pro=1
        right_pro=1
        n=len(nums)
        max_pro=float('-inf')
        for i in range(n):
            left_pro*=nums[i]
            right_pro*=nums[n-1-i]
            max_pro=max(max_pro,left_pro,right_pro)
            if left_pro==0:
                left_pro=1
            elif right_pro==0:
                right_pro=1
        return max_pro

        