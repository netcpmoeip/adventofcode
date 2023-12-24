data = open("./inputs/1.txt", "r").read()

result = 0
for line in data.split("\n"):
    arr = []
    for i, char in enumerate(line):
        if char.isdigit():
            arr.append(char)
        for j, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(value):
                arr.append(j+1)
    num = int(str(arr[0]) + str(arr[-1]))
    result += num
print(result)