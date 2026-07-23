class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_res=[]
        t_res=[]

        for letter in s:
            if letter=='#':
                if len(s_res)>0 :
                    s_res.pop()
            else:
                s_res.append(letter)

        for letter in t:
            if letter=='#':
                if len(t_res)>0:
                    t_res.pop()
            else:
                t_res.append(letter)
        if s_res==t_res:
            return True
        else:
            return False

