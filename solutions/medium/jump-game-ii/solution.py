from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        possible={len(nums)-1}
        seen = set()
        ittr=0
        while 0 not in possible:
            ittr+=1
            for k in set(possible):
                if k in seen:
                    continue
                toAdd= self.findPossibleLocations(nums,k)
                for element in toAdd:
                    possible.add(element)
                seen.add(k)




        return ittr

    def findPossibleLocations(self,nums,curLocation):

        possible=set()
        lowerBound=max(0,curLocation-1003)
        upperBound=min(len(nums)-1,curLocation+1003)
        for i in range(lowerBound,upperBound):
            if curLocation-nums[i]-i<=0:
                possible.add(i)
        return possible

