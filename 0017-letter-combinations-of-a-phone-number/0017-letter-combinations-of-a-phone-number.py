
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []

        if not digits:
            return result

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def solve(i, path):
            if i == len(digits):
                result.append(path)
                return

            letters = mapping[digits[i]]

            for ch in letters:
                solve(i + 1, path + ch)

        solve(0, "")
        return result
