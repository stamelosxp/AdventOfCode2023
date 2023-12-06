def part1(listfile):
    sumRes = 0
    for row in listfile:
        tmpsplit = row.split(':')
        tmpsplit = tmpsplit[1].split('|')

        tmpset1 = set(tmpsplit[0].split(' '))
        tmpset2 = set(tmpsplit[1].split(' '))
        tmpintersection  = tmpset1.intersection(tmpset2)
        tmplen = len(tmpintersection)-1

        if tmplen>0:
            sumRes += 1 * pow(2, tmplen-1)

    return sumRes
def part2(listfile,countList):
    countList = countList
    for idx, line in enumerate(listfile):
        tmpsplit = line.split(':')
        tmpsplit = tmpsplit[1].split('|')

        tmpset1 = set(tmpsplit[0].split(' '))
        tmpset2 = set(tmpsplit[1].split(' '))
        tmpintersection = tmpset1.intersection(tmpset2)
        tmplen = len(tmpintersection) - 1

        if tmplen > 0:
                for j in range(1, tmplen + 1):
                    for k in range(0, countList[idx]):
                        countList[idx+j]+=1

                    if j == len(listfile):
                        break
    return sum(countList)




if __name__ == '__main__':
    file = open('day4.txt', 'r')
    listfile = []
    countList= []
    for line in file:
        line = line.replace('\n','')
        listfile.append(line)
        countList.append(1)

    file.close()
    print(f"The answer for part1 is {part1(listfile)}")
    print(f"The answer for part1 is {part2(listfile, countList)}")