class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mydict={}

        for ch in magazine:
            mydict[ch]=mydict.get(ch,0)+1

        for ch in ransomNote:
            if ch not in magazine or mydict[ch]==0:
                return False

            mydict[ch]-=1
        return True
