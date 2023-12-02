def extractNumber(str):
    num = ''
    for char in str:
        if char.isdigit():
            num+=char

    return int(num)



def part1(listfile):
    sumID = 0
    for row in listfile:
        tmprow = row.split(':')
        id = extractNumber(tmprow[0])
        tmprow1 = tmprow[1].split(';')
        check=0
        for row in tmprow1:
            for i in row.split(','):
                if 'blue' in i:
                    if extractNumber(i) > 14:
                        check = 1
                if 'green' in i:
                    if extractNumber(i) > 13:
                        check = 1
                if 'red' in i:
                    if extractNumber(i) > 12:
                        check = 1

        if check == 0:
            sumID += id
    return sumID

def part2(listfile):
    sumRes= 0
    for row in listfile:
        tmprow = row.split(':')
        id = extractNumber(tmprow[0])
        tmprow1 = tmprow[1].split(';')
        tmpblue = 0
        tmpred = 0
        tmpgreen = 0
        for row in tmprow1:
            for i in row.split(','):
                if 'blue' in i:
                    if extractNumber(i) > tmpblue:
                        tmpblue = extractNumber(i)
                if 'green' in i:
                    if extractNumber(i) > tmpgreen:
                        tmpgreen = extractNumber(i)
                if 'red' in i:
                    if extractNumber(i) > tmpred:
                        tmpred = extractNumber(i)

        mul = tmpred * tmpgreen * tmpblue

        sumRes +=mul

    return sumRes


if __name__ == '__main__':
    file = open('day2.txt', 'r')
    listfile = []
    for row in file:
        listfile.append(row)
    file.close()

    print(f"The answer for part1 is {part1(listfile)}")
    print(f"The answer for part2 is {part2(listfile)}")
