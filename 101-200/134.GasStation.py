class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        n= len(gas)

        reserve=0
        index=0
        for i in range(n):
            reserve+=gas[i]-cost[i]
            if reserve <0:
                reserve, index= 0, i+1

        return index