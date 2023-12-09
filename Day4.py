with open('data/data4.dat') as data:
    lines = [line[:-1] for line in data]

# grid = [[c for c in line] for line in lines]
winnums = [line[10:40].strip().replace('  ', ' ').split(' ') for line in lines]
#winnums = [line[7:23].strip().replace('  ', ' ').split(' ') for line in lines]
winnums = [[int(c) for c in line] for line in winnums]
mynums = [line[42:].strip().replace('  ', ' ').split(' ') for line in lines]
#mynums = [line[25:].strip().replace('  ', ' ').split(' ') for line in lines]
mynums = [[int(c) for c in line] for line in mynums]
# print(winnums, mynums)
totalwin = 0

for i in range(len(winnums)):
    win = 0
    for num in mynums[i]:
        if win==0 and num in winnums[i]:
            win = 1
        elif win > 0 and num in winnums[i]:
            win = win*2
    totalwin += win


counter = 0


def refund(card):
    global counter
    counter += 1
    wins = checkwins(card)
    if wins == 0:
        return
    for i in range(card+1, card + wins + 1):
        #print(i)
        refund(i)
    return


def checkwins(card):
    wins = 0
    for num in mynums[card-1]:
        if num in winnums[card-1]:
            wins += 1
    return wins


for i in range(len(winnums)):
    refund(i)
print(counter)
