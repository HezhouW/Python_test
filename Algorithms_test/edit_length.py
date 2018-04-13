##参考https://www.python-course.eu/levenshtein_distance.php
## Levenshtein Distance 算法：编辑距离的计算

def edit_length(s,t):
    row = len(s)+1
    colum = len(t)+1

    dist = [[0 for x in range(colum)] for y in range(row)]

    for x in range(1,row):
        dist[x][0] = x
    for y in range(colum):
        dist[0][y] = y

    for i in range(1, row):
        for j in range(1,colum):
            cost = 0
            if s[i-1] == t[j-1]:
                cost = 0
            else:
                cost = 1  # 最后一个字符是相同的，则不用改变。
            dist[i][j] = min(dist[i-1][j]+1, dist[i][j-1]+1, dist[i-1][j-1]+cost)
        for x in range(row):
            print(dist[x])
        print('-----------------')
    for x in range(row):
        print(dist[x])
    return dist[row-1][colum-1]

if __name__ == '__main__':
    s = 'whz'
    t = 'zhangqian'
    print(edit_length(s, t))
