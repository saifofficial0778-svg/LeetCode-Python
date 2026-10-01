class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        stack=[]
        res=[-1]*n
        for i in range(2*n-1,-1,-1):
            idx=i%n
            while stack and stack[-1]<=nums[idx]:
                stack.pop()

            if i<n:
                if stack:
                    res[idx]=stack[-1]

            stack.append(nums[idx])
        return res

