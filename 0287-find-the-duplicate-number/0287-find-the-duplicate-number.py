class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set()

        for i in range(0,n):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return nums[i]
       
        