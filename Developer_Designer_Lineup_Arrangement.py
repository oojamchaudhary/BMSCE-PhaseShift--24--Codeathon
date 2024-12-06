m = 10 ** 9 + 7
def total_num(a, b, c, d):
    table = [[[0, 0] for _ in range(b + 1)] for _ in range(a + 1)]
    table[0][0][0] = 1 
    table[0][0][1] = 1 

    for i in range(a + 1):
        for j in range(b + 1):
        
            for k in range(1, c + 1):
                if i >= k:
                    table[i][j][0] += table[i - k][j][1]
                    table[i][j][0] %= m      
            for k in range(1, d + 1):
                if j >= k:
                    table[i][j][1] += table[i][j - k][0]
                    table[i][j][1] %= m
    return (table[a][b][0] + table[a][b][1]) % m

a, b, c, d = map(int, input().split())
print(total_num(a, b, c, d))