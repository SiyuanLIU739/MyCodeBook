lines = ["1,2,3,2,1,1,2,4,8,2,2,4,5;3"]

for line in lines:
    p = [0]
    k = 0
    
    for i in range(len(line)):
        if(line[i] == ','):
            continue
        if(line[i] == ';'):
            k = int(line[i + 1:])
            break
        
        for j in range(i + 1, len(line)):
            if(line[j] == ',' or line[j] == ';'):
                p.append(int(line[i: j]))
                break

    n = len(p) - 1
    inf = 2147483647
    
    f = []
    for i in range(n + 1):
        lst = []
        for j in range(k + 1):
            lst.append([-inf, -inf])
        f.append(lst)

    f[0][0][0] = 0

    ans = -inf
    ansk = inf
    for i in range(1, n + 1):
        for j in range(k + 1):
            f[i].append([f[i - 1][j][0], f[i - 1][j][1]])
            for l in range(i):
                f[i][j][1] = max(f[i][j][1], f[l][j][0] - p[i])

                if(j >= 1):
                    f[i][j][0] = max(f[i][j][0], f[l][j - 1][1] + p[i])

            if(f[i][j][0] > ans):
                ans = f[i][j][0]
                ansk = j

            elif(f[i][j][0] == ans):
                ansk = min(ansk, j)

    s = "{},{}"
    print(s.format(ans, ansk), end = "")
