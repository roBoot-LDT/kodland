s = input("WRITE DOWN THIS SHIT: ")
levels = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
maxLevel = levels[s[0]]
answer = maxLevel
firstIteration = True
for number in range(1, len(s)): #III
    if firstIteration:
        if levels[s[number]] > maxLevel:
            answer += levels[s[number]] - (2*maxLevel)
            firstIteration = False
        else:
            answer += levels[s[number]]
            firstIteration = False


    elif levels[s[number]] > maxLevel:
        answer += levels[s[number]] - maxLevel
    else:
        answer += levels[s[number]]

print(answer)
