class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mydict={}
        for ch in text:
            mydict[ch]=mydict.get(ch,0)+1

        b=mydict.get('b',0)
        a=mydict.get('a',0)
        l=mydict.get('l',0)//2
        o=mydict.get('o',0)//2
        n=mydict.get('n',0)

        return min(b,a,l,o,n)