if __name__ == "__main__":
    file = open('input.txt')
    letlist = []
    x, total = 0, 0
    fstr = file.read().split("\n")
    while x < len(fstr):
        for let in fstr[x]:
            for cmplet in fstr[x+1]:
                if let == cmplet:
                    letlist.append(let)
        for let in letlist:
            for cmplet in fstr[x+2]:
                if let == cmplet:
                    finlet = let
        if finlet.islower():
            finlet = ord(finlet) - 96
        elif finlet.isupper():
            finlet = ord(finlet) - 38
        total += finlet
        letlist = []
        x += 3
    print(total)

'''Part 1
    file = open('input.txt')
    dup = ""
    total = 0
    for line in file:
        length = len(line)//2
        str1 = line[:length]
        str2 = line[length:]
        for let1 in str1:
            for let2 in str2:
                if let1 == let2:
                    dup = let1
        if dup.islower():
            dup = ord(dup) - 96
        elif dup.isupper():
            dup = ord(dup) - 38
        total += dup
        dup = 0
    print(total)
'''

