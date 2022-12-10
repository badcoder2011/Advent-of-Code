if __name__ == "__main__":
    file = open('input.txt')
    string = file.readline()
    test = string[0:4]
    count, x = 0, 0
    for word in string:
        for let in test:
            if count == 4:
                break
            elif test.find(let, test.find(let)+1) == -1:
                count += 1
            else:
                count = 0
        if count == 4:
            break
        else:
            count = 0
        x += 1
        test = string[x:x + 4]

    print(x+4)