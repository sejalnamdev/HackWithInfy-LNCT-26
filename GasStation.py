class Solution:
    def canCompleteCircuit(self, gas, cost):
        total = 0
        curr_tank = 0
        start = 0
        
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total += gain
            curr_tank += gain
            
            # If tank goes negative → change starting point
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        
        # If overall gas is enough
        return start if total >= 0 else -1