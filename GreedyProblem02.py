class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        
        prices.sort()
        
        #Maxprice
        maxi=0;
        buy=len(prices)-1
        free=0
        
        while free<=buy :
            maxi=maxi+ prices[buy]
            buy-=1
            free+=k
            
        
        #Minprice
        mini=0
        buy=0
        free=len(prices)-1
        
        while buy<=free :
            mini=mini+prices[buy]
            buy+=1
            free-=k
            
        
        return [mini,maxi]
        
            
        