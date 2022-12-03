if __name__ == "__main__":
    file = open('input.txt')
    maxelf = [0, 0, 0]
    curelf = 0
    for line in file:
        if line == "\n":
            if maxelf[0] < curelf:
                maxelf.insert(0, curelf)
                maxelf.pop()
            elif maxelf[1] < curelf:
                maxelf.insert(1, curelf)
                maxelf.pop()
            elif maxelf[2] < curelf:
                maxelf.insert(2, curelf)
                maxelf.pop()
            curelf = 0
        else:
            curelf += int(line)
    print(maxelf)
    print(sum(maxelf))


'''Part 1
file = open('input.txt')
    maxelf = [0,0]
    curelf = [0,0]
    for line in file:
        if line == "\n":
            curelf[1] += 1
            if maxelf[0] < curelf[0]:
                maxelf[0] = curelf[0]
                maxelf[1] = curelf[1]
            curelf[0] = 0
        else:
            curelf[0] += int(line)
    print(maxelf)
'''