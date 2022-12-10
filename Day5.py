if __name__ == "__main__":
    file = open('input.txt')
    lists = [[],[],[],[],[],[],[],[],[]]
    move = []
    count, list = 0, 0
    line = file.readline()
    while line.find("1") == -1:
        count, list = 0, 0
        while count < len(line):
            if ((count-1)%4) == 0:
                if line[count].isalpha():
                    lists[list].append(line[count])
                list += 1
            count += 1
        line = file.readline()
    print(lists)
    count = 0
    line = file.readline()
    line = file.readline()
    while len(line) != 0:
        spline = line.strip("\n").split(" ")
        count = 0
        for count in range(int(spline[1])):
            lists[int(spline[5])-1].insert(0, lists[int(spline[3])-1].pop(int(spline[1])-count-1))
            # For part one just pop(0)
            # lists[int(spline[5])-1].insert(0, lists[int(spline[3])-1].pop(0))
            count += 1
        line = file.readline()
    print(lists)