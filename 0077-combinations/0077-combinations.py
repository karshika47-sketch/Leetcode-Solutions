class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        r1=[]
        comb=[]
        def back(start):
            if len(comb)==k:
                r1.append(comb[:])
                return 
            for num in range(start,n+1):
                comb.append(num)
                back(num+1)
                comb.pop()
        back(1)
        return r1            
        