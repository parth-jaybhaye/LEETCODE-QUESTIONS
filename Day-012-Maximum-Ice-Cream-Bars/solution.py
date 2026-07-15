class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()

        for i in range(len(costs)):
            if coins >= costs[i]:
                coins -= costs[i]
            else:
                return i

        return len(costs)