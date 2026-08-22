class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        max_pro=float('-inf')
        left_pro=1
        right_pro=1
        for i in range(n):
            left_pro*=nums[i]
            right_pro*=nums[n-i-1]
            max_pro=max(left_pro,right_pro,max_pro)

            if left_pro==0:
                left_pro=1
            if right_pro==0:
                right_pro=1

        return max_pro

            