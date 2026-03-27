class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                if count > 0:
                    break
                i-=1
            
            else:
                count += 1
        return count 
        
