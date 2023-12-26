data = open("./inputs/2.txt", "r").read()
valid = {'red': 12, 'green': 13, 'blue': 14}
result_1 = 0
result_2 = 0

for i, line in enumerate(data.split("\n")):
    games = line.split(":")[1]
    possible = True
    maxs = {"red": 0, "green": 0, "blue": 0}
    for game in games.split(";"):
        arr = {}
        for set in game.split(","):
            num,color = set[1:].split(" ")
            arr[color] = num
            if int(num) > valid.get(color):
                possible = False
            
            maxs[color] = max(maxs[color], int(num))
    if possible == True:
        result_1 += i+1
    
    s = 1
    for x in maxs.values():
        s *= int(x)
    result_2 += s
print(result_1)
print(result_2)

        
