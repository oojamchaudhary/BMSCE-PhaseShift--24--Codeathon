def tower(i, n, H):
    m = 10**9 + 7
    table = [0] * (H + 1)
    table[0] = 1
    for p in range(i):
        newtable = [0] * (H + 1)
        presum = 0
        for H in range(0, H + 1):
            presum += table[H]
            if H > n:
                presum -= table[H - n - 1]
            newtable[H] = presum % m
        table = newtable
    return table[H] if table[H] > 0 else -1
i, n, h = map(int, input().split())
print(tower(i, n, h))