def part1(listfile):
    sumNum = 0

    for row in listfile:
        tmplist = []
        charslist = [*row]
        for char in charslist:
            if char.isdigit():
                tmplist.append(char)
        if len(tmplist) == 1:
            num = str(tmplist[0]) + str(tmplist[0])
        else:
            num = str(tmplist[0]) + str(tmplist[len(tmplist) - 1])

        sumNum += int(num)

    return sumNum

def part2(listfile):
    sumNum = 0
    listnum = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    for i in listfile:
        tmpchar = ''
        tmplist = []
        charslist = [*i]
        for char in charslist:
            if char.isdigit():
                tmplist.append(char)
                tmpchar = ''
            else:
                tmpchar += str(char)
                for strnum in listnum:
                    if strnum in tmpchar:
                        tmpnum = getNum(strnum)
                        tmplist.append(str(tmpnum))
                        tmpchar = ''
        lastnum = str(tmplist[0]) + str(tmplist[len(tmplist) - 1])
        sumNum += int(lastnum)
    return sumNum
def getNum(strnum):
    if strnum == 'one':
        return 1
    elif strnum == 'two':
        return 2
    elif strnum == 'three':
        return 3
    elif strnum == 'four':
        return 4
    elif strnum == 'five':
        return 5
    elif strnum == 'six':
        return 6
    elif strnum == 'seven':
        return 7
    elif strnum == 'eight':
        return 8
    else:
        return 9

if __name__ == '__main__':

    file = open('day1.txt', 'r')
    listfile = []
    for row in file:
        listfile.append(row)
    file.close()
    print(f"The answer for part1 is {part1(listfile)}")
    print(f"The answer for part2 is {part2(listfile)}")

