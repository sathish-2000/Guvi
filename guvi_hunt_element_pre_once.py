L = map(str,raw_input().split())
K = list(set(L))
for i in K:
    if L.count(i) == 1 :
        print i
        break
