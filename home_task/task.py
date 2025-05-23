import timeit


def find_coins_greedy(amount, coins):

    result = {}
    for coin in coins:
        count = amount // coin
        if count:
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount, coins):

    if amount <= 0:
        return {}
    min_coins = [0] + [float('inf')] * amount
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


if __name__ == "__main__":

    coins = [50, 25, 10, 5, 2, 1]
    # coins = [50, 25, 10, 5, 2]

    greedy_time = timeit.timeit(
        lambda: find_coins_greedy(113, coins), number=1)
    dp_time = timeit.timeit(lambda: find_min_coins(113, coins), number=1)
    greedy_res = find_coins_greedy(113, coins)
    dp_res = find_min_coins(113, coins)

    print("\n|---------------------|----------------------------|-------------------|")
    print("|      Алгоритм       |         Результат          | Час виконання (с) |")
    print("|---------------------|----------------------------|-------------------|")
    print(
        f"| Жадібний (Greedy)   | {greedy_res} |   {greedy_time:.12f}  |")
    print("|---------------------|----------------------------|-------------------|")
    print(
        f"| Динамічний (DP)     | {dp_res} |   {dp_time:.12f}  |")
    print("|---------------------|----------------------------|-------------------|\n")
