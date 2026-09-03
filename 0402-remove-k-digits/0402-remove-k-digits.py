class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for no in num:
            while stack and k > 0 and stack[-1] > no:
                stack.pop()
                k -= 1

            stack.append(no)

        while k > 0:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip("0")

        return result if result else "0"