if __name__ == "__main__":
    file = open('input.txt')
    total = 0
    nums = [3,1,2]
    # part 2
    for line in file:
        line = line.split()
        num1 = ord(line[0]) - 64
        num2 = ord(line[1]) - 87
        if(num2 == 1):
            total += nums[((num1 + 2) % 3)]
            print("L")
        elif (num2 == 2):
            total += num1
            total += 3
            print("D")
        elif (num2 == 3):
            total += nums[((num1 + 1) % 3)]
            total += 6
            print("W")
        print(total)

    print(total)

""" PART 1
    for line in file:
        line = line.split()
        num1 = ord(line[0]) - 64
        num2 = ord(line[1]) - 87
        total += num2
        if(num1 == num2):
            total += 3
        elif(num1 == 1 and num2 == 2):
            total += 6
        elif(num1 == 2 and num2 == 3):
            total += 6
        elif(num1 == 3 and num2 == 1):
            total += 6
"""