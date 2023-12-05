def isPartNumber(matrix):
    rownums = []
    rowsyms = []
    currnums = []
    currsyms = []
    partSum = 0
    for row in range(len(matrix)):
        lastrownums = currnums
        lastrowsyms = currsyms
        i = len(matrix[row]) - 1
        currnums = []
        currsyms = []
        while i>0:
            #print(i)
            if matrix[row][i].isdigit():
                cont = numberIs(matrix[row][:(i + 1)])
                i = cont[0] + 1
                currnums = [[cont[1], max(0, i-1), min(i + cont[2], len(matrix[row]) - 1)]] + currnums
            elif matrix[row][i] != '.':
                currsyms = [i] + currsyms
            i -= 1
        rownums.append(currnums)
        rowsyms.append(currsyms)
        partSum += checkAdjacency(lastrowsyms, lastrownums, currsyms, currnums)
    print('nums in matrix:', rownums)
    print('symbols in matrix:', rowsyms)
    return partSum


def numberIs(row):
    i = len(row) - 1
    num = 0
    cycle = 0
    while i>=0 and row[i].isdigit():
        num += int(row[i])*10**(cycle)
        cycle += 1
        i -= 1
    return [i, num, cycle]


def checkAdjacency(ls, ln,  cs, cn):
    adjacent = 0
    if len(cn) != 0:
        for i in range(len(cn)):
            for sym in ls:
                if cn[i][1] <= sym <= cn[i][2]:
                    #print(cn[i][0])
                    adjacent += cn[i][0]
            for sym in cs:
                if cn[i][1] <= sym <= cn[i][2]:
                    #print(cn[i][0])
                    adjacent += cn[i][0]
    if len(ln) != 0:
        for i in range(len(ln)):
            for sym in cs:
                if ln[i][1] <= sym <= ln[i][2]:
                    #print(ln[i][0])
                    adjacent += ln[i][0]
    return adjacent


with open('data/data3') as data:
    matrix = []
    for line in data:
        matrix.append(line[:-1])
    print(isPartNumber(matrix))


print()
