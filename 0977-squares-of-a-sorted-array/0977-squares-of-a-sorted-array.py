class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        pos=n-1

        left=0
        right=n-1

        while left<=right:
            left_sqr=nums[left]*nums[left]
            right_sqr=nums[right]*nums[right]

            if left_sqr>right_sqr:
                ans[pos]=left_sqr
                pos-=1
                left+=1
            else:
                ans[pos]=right_sqr
                pos-=1
                right-=1
        return ans

        