#User function Template for python3

class Solution:
    def minimumDays(self, S, N, M):
        # code here
        if S>=7 and 6 * N < 7 * M:
            return -1
            
        Sunday = S//7
        
        Buyingdays = S-Sunday
        
        Totalfood = S*M
        
        
        
        if Totalfood%N == 0:
            ans = Totalfood//N
        else:
            ans = (Totalfood//N) + 1
            
        if ans <= Buyingdays:
            return ans
        else:
            return -1
        
        