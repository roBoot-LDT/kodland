s = input("WRITE DOWN THIS SHIT: ")
levels = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
answer = 0
skipIteration = False
for number in range(len(s)):
    if not skipIteration:
        if number == len(s) - 1:
            answer += levels[s[number]]
        elif levels[s[number]] < levels[s[number+1]]:
            answer += levels[s[number+1]] - levels[s[number]]
            skipIteration = True
        else:
            answer += levels[s[number]]
    else:
        skipIteration = False
        continue

print(answer)









































# maxLevel = levels[s[0]]
# answer = maxLevel
# firstIteration = True
# for number in range(1, len(s)): #III
#     if firstIteration:
#         if levels[s[number]] > maxLevel:
#             answer += levels[s[number]] - (2*maxLevel)
#             firstIteration = False
#         else:
#             answer += levels[s[number]]
#             firstIteration = False


#     elif levels[s[number]] > maxLevel:
#         answer += levels[s[number]] - maxLevel
#     else:
#         answer += levels[s[number]]

# print(answer)
