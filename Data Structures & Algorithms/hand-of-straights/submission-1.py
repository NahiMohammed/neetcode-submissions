class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counter = Counter(hand)

        for num in sorted(counter):
            occ = counter[num]

            if occ > 0:
                for i in range(1, groupSize):
                    if counter[num + i] < occ:
                        return False
                    counter[num + i] -= occ

        return True