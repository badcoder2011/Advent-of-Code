import re
if __name__ == "__main__":
    file = open('input.txt')
    total = 0
    for line in file:
        numstr = re.findall(r'\d+', line)
        nums = list(map(int, numstr))
        if len(set(range(nums[0], nums[1]+1)).intersection(set(range(nums[2], nums[3]+1)))) != 0:
            total += 1
    print(total)

    '''Part 1
import re
if __name__ == "__main__":
    file = open('input.txt')
    total = 0
    for line in file:
        numstr = re.findall(r'\d+', line)
        nums = list(map(int, numstr))
        if set(range(nums[0], nums[1]+1)).issubset(set(range(nums[2], nums[3]+1))):
            total += 1
        elif set(range(nums[2], nums[3]+1)).issubset(set(range(nums[0], nums[1]+1))):
            total += 1
    print(total)
    '''