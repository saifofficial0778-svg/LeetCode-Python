class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict={}

        for word in strs:
            letter="".join(sorted(word))
            if letter not in mydict:
                mydict[letter]=[]
            mydict[letter].append(word)
        return list(mydict.values())