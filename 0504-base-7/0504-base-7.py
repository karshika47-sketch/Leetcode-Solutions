class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        resi=""
        n=abs(num)
        while(n>0):
            resi+=str(n%7)
            n//=7
        resi=resi[::-1]
        if num<0:
            resi="-"+resi
        return resi        


        