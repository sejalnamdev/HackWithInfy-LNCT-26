import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.mp = {}

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        
        self.mp[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        
        idx = self.mp[val]
        last = self.nums[-1]
        
        # swap
        self.nums[idx] = last
        self.mp[last] = idx
        
        # remove last
        self.nums.pop()
        del self.mp[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)