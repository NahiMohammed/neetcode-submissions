class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_gas =0
        res=0
        not_possible=False
        for i in range(len(gas)) :
            curr_gas=gas[i]
            not_possible=False
            for j in range(1,len(gas)+1):
                if cost[(i+j-1)%len(gas)]> curr_gas :
                    not_possible=True
                    break
                curr_gas= curr_gas + gas[(i+j)%len(gas)]-cost[(i+j-1)%len(gas)]

            if not not_possible :
                return i
        return -1
                



        