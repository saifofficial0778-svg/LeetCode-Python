class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n

        def reverse(first , last):
            while first < last:
                nums[first],nums[last]=nums[last],nums[first]
                first+=1
                last-=1

        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)