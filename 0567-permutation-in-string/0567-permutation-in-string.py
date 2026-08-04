class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mydict={}
        n=len(s1)
        left=0
        for i in range(0,n):
            if s1[i] not in mydict:
                mydict[s1[i]]=1
            else:
                mydict[s1[i]]+=1
        temp={}
        for right in range(len(s2)):
            if s2[right] not in temp:
                temp[s2[right]]=1
            else:
                temp[s2[right]]+=1
            while right-left+1>n:
                temp[s2[left]]-=1
                if temp[s2[left]]==0:
                    del temp[s2[left]]
                left+=1
            if temp==mydict:
                return True
        return False
        
                



        