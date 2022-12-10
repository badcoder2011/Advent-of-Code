if __name__ == "__main__":
    file = open('input.txt')
    string = file.readline()
    test = string[0:14]
    count, x = 0, 0
    for word in string:
        for let in test:
            if count == 14:
                break
            elif test.find(let, test.find(let)+1) == -1:
                count += 1
            else:
                count = 0
        if count == 14:
            break
        else:
            count = 0
        x += 1
        test = string[x:x + 14]

    print(x+14)

    # For part 1 just change all 14's to 4's