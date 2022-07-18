from typing import List


class Solution:
    def maxProfit(self,prices:List[int]):
        l,r=0,1
        maxP=0
        while r< len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l=r
            r += 1

        return maxP


if __name__ == "__main__":
    # prices = [7,1,5,3,6,4]
    prices = [7,6,4,3,1]
    s = Solution()
    print(s.maxProfit(prices))
    

