def isPossible(game):
    draws = game.split('; ')
    maxr, maxg, maxb = 12, 13, 14
    for draw in draws:
        r, g, b = 0, 0, 0
        draw = draw.split(', ')
        #print(draw)
        for counts in draw:
            counts = counts.split(' ')
            #print(counts)
            if counts[1]=='red':
                r = int(counts[0])
            elif counts[1]=='green':
                g = int(counts[0])
            elif counts[1]=='blue':
                b = int(counts[0])
        #print(r, g, b)
            if r>maxr or g>maxg or b>maxb:
                return False
    return True


def power(game):
    draws = game.split('; ')
    maxr, maxg, maxb = 0, 0, 0
    for draw in draws:
        r, g, b = 0, 0, 0
        draw = draw.split(', ')
        #print(draw)
        for counts in draw:
            counts = counts.split(' ')
            #print(counts)
            if counts[1]=='red':
                r = int(counts[0])
            elif counts[1]=='green':
                g = int(counts[0])
            elif counts[1]=='blue':
                b = int(counts[0])
            cubes = [r, g, b]
        maxr, maxg, maxb = max(cubes[0], maxr), max(cubes[1], maxg), max(cubes[2], maxb)
        pow = maxr*maxg*maxb
    return pow


with open('data/data2') as data:
    answer = 0
    sumPowers = 0
    for line in data:
        games = line[:-1].split(': ')
        num = int(games[0][5:])
        if isPossible(games[1]):
            answer += num
        sumPowers += power(games[1])

    print(answer)
    print(sumPowers)
