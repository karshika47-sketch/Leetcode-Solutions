class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        min1=min(op[0] for op in ops)
        min2=min(op[1] for op in ops)
        return min1*min2    
        