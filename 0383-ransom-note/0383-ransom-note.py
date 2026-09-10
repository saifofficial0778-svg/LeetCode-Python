class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        source = {}

        for ch in magazine:
            source[ch] = source.get(ch, 0) + 1

        for ch in ransomNote:
            if ch not in source or source[ch] == 0:
                return False

            source[ch] -= 1

        return True