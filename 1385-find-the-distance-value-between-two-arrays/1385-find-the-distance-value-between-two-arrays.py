class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        res=0
        for a in arr1:
            low=0
            high=len(arr2)-1
            found=False
            while low<=high:
                mid=low+(high-low)//2
                if a-d<=arr2[mid]<=a+d:
                    found=True
                    break
                elif arr2[mid]<a-d:
                    low=mid+1
                else:
                    high=mid-1
            if not found:
                res+=1
        return res                        