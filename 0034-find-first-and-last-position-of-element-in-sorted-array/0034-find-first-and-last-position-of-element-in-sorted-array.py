class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        low1, high1 = 0, n - 1
        low2, high2 = 0, n - 1

        first = -1
        ceil = -1

        
        while low1 <= high1:
            mid1 = (low1 + high1) // 2

            if nums[mid1] >= target:
                first = mid1
                high1 = mid1 - 1
            else:
                low1 = mid1 + 1

        
        while low2 <= high2:
            mid2 = (low2 + high2) // 2

            if nums[mid2] > target:
                ceil = mid2
                high2 = mid2 - 1
            else:
                low2 = mid2 + 1

        if first == -1 or nums[first] != target:
            return [-1, -1]
        if ceil==-1:
            return [first,n-1]

        return [first, ceil - 1]