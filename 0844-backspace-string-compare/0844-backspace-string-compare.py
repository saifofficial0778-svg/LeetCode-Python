class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1=len(s)-1
        p2=len(t)-1
        s_skip=0
        t_skip=0

        while p1>=0 or p2>=0:

            while p1>=0:
                if s[p1]=='#':
                    s_skip+=1
                    p1-=1
                elif s_skip>0:
                    s_skip-=1
                    p1-=1
                else:
                    break
            while p2>=0:
                if t[p2]=='#':
                    t_skip+=1
                    p2-=1
                elif t_skip>0:
                    t_skip-=1
                    p2-=1
                else:
                    break
            if p1>=0 and p2>=0:
                if s[p1]!=t[p2]:
                    return False
            elif (p1>=0 and p2<0) or (p2>=0 and p1<0):
                return False
            p1-=1
            p2-=1
        return True


            
