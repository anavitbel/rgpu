def squareSequenceDigit(n):
    l_all = []
    i = 1

    while len(l_all) < n:
        l_add = []
        i_sq = i * i
        while i_sq > 0:
            l_add.append(i_sq % 10)
            i_sq = i_sq // 10
        l_add = l_add[::-1]
        l_all += l_add
        i += 1

    return(l_all[n - 1])