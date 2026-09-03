class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mydict={}
        for i in range(len(p)):
            if p[i] not in mydict:
                mydict[p[i]]=1
            else:
                mydict[p[i]]+=1
        temp={}
        left=0
        res=[]
        for right in range(len(s)):
            if s[right] not in temp:
                temp[s[right]]=1
            else:
                temp[s[right]]+=1
            while (right-left+1)>len(p):
                temp[s[left]]-=1
                if temp[s[left]]==0:
                    del temp[s[left]]
                left+=1
            if temp==mydict:
                res.append(left)
        return res
                