class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need={}
        for i in range(0,len(p)):
            if p[i] not in need:
                need[p[i]]=1
            else:
                need[p[i]]+=1
        left=0
        ans=[]
        temp={}
        for right in range(0,len(s)):
            if s[right] not in temp:
                temp[s[right]]=1
            else:
                temp[s[right]]+=1

            while (right-left+1)>len(p):
                temp[s[left]]-=1
                if temp[s[left]]==0:
                    del temp[s[left]]

                left+=1
            if temp==need:
                ans.append(left)
        return ans