t = (int)(input())
while t > 0:
    cases = input()
    cases = list(int(i) for i in cases.split())
    n = cases[0]
    m = cases[1]
    li = input()
    li = list(int(i) for i in li.split())
    if li.count(li[0]) >= m and li.count(li[-1])>=m:
        print("YES")
    else:
        print("NO")
    t -= 1