class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = 0
        if need1 <= need2:
            ans += costBoth * need1
            if cost2 <= costBoth:
                ans += (need2 - need1) * cost2
            else:
                ans += (need2 - need1) * costBoth
        else:
            ans += costBoth * need2
            if cost1 <= costBoth:
                ans += (need1 - need2) * cost1
            else:
                ans += (need1 - need2) * costBoth
        if ans <= (cost1 * need1) + (cost2 * need2):
            return ans
        else:
            return (cost1 * need1) + (cost2 * need2)