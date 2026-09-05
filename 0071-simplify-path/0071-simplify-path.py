class Solution:
    def simplifyPath(self, path: str) -> str:
        res=path.split('/')
        stack=[]
        for i in range(len(res)):
            if res[i]=="" or res[i]==".":
                continue
            elif res[i]=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(res[i])
        return "/" + "/".join(stack)