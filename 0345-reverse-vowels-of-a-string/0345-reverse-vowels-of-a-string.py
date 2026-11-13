class Solution:
    def reverseVowels(self, s: str) -> str:
        word=list(s)
        stt=0
        end=len(s)-1
        v="aeiouAEIOU"
        while stt<end:
            while stt<end and v.find(word[stt])==-1:
                stt+=1
            while stt<end and v.find(word[end])==-1:
                end-=1
            word[stt],word[end]=word[end],word[stt]
            stt+=1
            end-=1
        return "".join(word)            
        