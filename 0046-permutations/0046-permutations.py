class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def solve(path, used):
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True

                    solve(path, used)

                    path.pop()
                    used[i] = False

        used = [False] * len(nums)
        solve([], used)

        return result