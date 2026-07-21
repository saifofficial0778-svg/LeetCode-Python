class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        pos=n-1
        res=[0]*n

        while left<=right:
            left_sqr=nums[left]*nums[left]
            right_sqr=nums[right]*nums[right]

            if left_sqr<right_sqr:
                res[pos]=right_sqr
                right-=1
                pos-=1
            else:
                res[pos]=left_sqr
                left+=1
                pos-=1
        return res