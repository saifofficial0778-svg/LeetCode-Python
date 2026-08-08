class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        mydict={}
        for i in range(0,len(words)):
            if words[i] not in mydict:
                mydict[words[i]]=1
            else:
                mydict[words[i]]+=1
    
        res=[]
        n=len(s)
        m=len(words)*len(words[0])
        for i in range(0,n-m+1):
            temp={}
            for j in range(i,i+m,len(words[0])):
                word=s[j:j+len(words[0])]
                if word not in temp:
                    temp[word]=1
                else:
                    temp[word]+=1
            if temp==mydict:
                res.append(i)
        return res