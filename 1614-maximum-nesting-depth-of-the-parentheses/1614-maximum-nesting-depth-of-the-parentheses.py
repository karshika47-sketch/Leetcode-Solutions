class Solution:
    def maxDepth(self, s: str) -> int:
        maxd=0
        count=0
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
            elif s[i]==')':
                count-=1
            maxd=max(maxd,count)
        return maxd            

        