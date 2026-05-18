class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            profit = prices[i] - min_price
            if max_profit < profit:
                max_profit = profit
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    test_prices = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {test_prices}")
    print(f"Max Profit: {sol.maxProfit(test_prices)}")
