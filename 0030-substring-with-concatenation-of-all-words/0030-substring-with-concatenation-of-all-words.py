class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        mydict={}
        res=[]
        for i in range(len(words)):
            if words[i] not in mydict:
                mydict[words[i]]=1
            else:
                mydict[words[i]]+=1

        word_len=len(words[0])
        for offset in range(word_len):
            temp={}
            left=offset
            count=0
            for right in range(offset,len(s),word_len):
                word=s[right:right+word_len]

                if word not in mydict:
                    temp={}
                    left=right+word_len
                    count=0
                    continue
                if word not in temp:
                    temp[word]=1
                else:
                    temp[word]+=1
                count+=1

                while temp[word] > mydict[word]:
                    left_word=s[left:left+word_len]
                    temp[left_word]-=1
                    count-=1
                    if temp[left_word]==0:
                        del temp[left_word]
                    left+=word_len

                if count==len(words):
                    res.append(left)
        return res

                

