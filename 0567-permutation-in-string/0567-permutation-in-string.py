class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mydict={}
        for i in range(0,len(s1)):
            if s1[i] not in mydict:
                mydict[s1[i]]=1
            else:
                mydict[s1[i]]+=1
        temp={}
        left=0
        for right in range(0,len(s2)):
            if s2[right] not in temp:
                temp[s2[right]]=1
            else:
                temp[s2[right]]+=1
            while right-left+1>len(s1):
                temp[s2[left]]-=1

                if temp[s2[left]]==0:
                    del temp[s2[left]]
                left+=1
            if temp==mydict:
                return True
        return False