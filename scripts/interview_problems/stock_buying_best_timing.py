from pathlib import Path

from scripts.interview_problems.common import load_data


def buy_sell_stock(prices: list):
    cum_min_price = []
    running_profit = []

    min_temp = prices[0]
    for x in prices:
        if x < min_temp:
            min_temp = x
        cum_min_price.append(min_temp)

    for i in range(0, len(prices), 1):
        running_profit.append(prices[i] - cum_min_price[i])

    return max(running_profit)


if __name__ == "__main__":
    data = load_data()
    prices = list(data["close"])
    prices = [7,1,5,3,6,4]
    buy_sell_stock(prices)
