def change(N, M1, S1, M2, S2, M3, S3, M4, S4):
    coins = [(S1, M1), (S2, M2), (S3, M3), (S4, M4)]
    coins.sort(reverse=True)
    ch = []

    for coin in coins:
        while N >= coin[0] and coin[1] > 0:
            N -= coin[0]
            coin = (coin[0], coin[1]-1)
            ch.append(coin[0])

        if N == 0:
            break

    if N != 0:
        print("Невозможно дать сдачу")
    else:
        print("Наименьшая комбинация монет:", ch)

change(123, 10, 50, 5, 20, 2, 5, 7, 1)