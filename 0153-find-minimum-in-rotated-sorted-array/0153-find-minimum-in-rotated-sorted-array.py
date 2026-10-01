class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        ans = nums[0]

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] <= nums[high]:
                ans = min(ans, nums[mid])
                high = mid - 1
            else:
                low = mid + 1

        return ans