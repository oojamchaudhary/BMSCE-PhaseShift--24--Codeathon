def solve():
    s, e = map(int, input().split())
    ev = [0] * e
    par = [0] * s
    for i in range(s):
        line = input().strip()
        inp = list(map(int, line.split()))  
        if inp and inp[0] != 0:
            for num in inp:
                ev[num - 1] += 1
            par[i] += len(inp)
    evcount = sum(1 for count in par if count > 0)
    parcount = sum(1 for count in ev if count > 0)
    print(min(evcount, parcount))
if __name__ == "__main__":
    solve()