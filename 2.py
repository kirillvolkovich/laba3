def steal(museum, N, M, K):
    museum.sort(key=lambda x: x[1] / x[0], reverse=True)
    stolen = []
    for i in range(M):
        weight_left = K
        for j in range(len(museum)):
            if museum[j][0] <= weight_left and museum[j] not in stolen:
                stolen.append(museum[j])
                weight_left -= museum[j][0]
                if len(stolen) == N:
                    return stolen
    return stolen


museum = [(2, 10), (3, 12), (1, 6), (4, 15), (2, 8), (5, 20), (1, 15), (3, 21)]
N = 5
M = 2
K = 7

stolen_items = steal(museum, N, M, K)
if len(stolen_items) == N:
    print('список украденных экспонатов:')
    for item in stolen_items:
        print("Вес:", item[0], "Цена:", item[1])
else:
    print('за', M, 'заходов не унести', N, 'экспонатов')


