#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        meetings = []
        
        for i in range(len(start)):
            meetings.append((start[i],end[i]))
            
        
        
        meetings.sort(key= lambda x: x[1])
        
        count = 1
        
        ansEnd = meetings[0][1]
        
        for i in range(len(meetings)):
            if meetings[i][0] > ansEnd:
                count+=1
                ansEnd = meetings[i][1]
                
        return count
            
            
        # code here