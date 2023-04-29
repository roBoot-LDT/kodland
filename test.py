from random import choice
letters = "1234567890!@#$%^&*()qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:ZXCVBNM<>?"
ques = input("Какой длины пароль? ")
answer = []
for letter in range(int(ques)):
    answer.append(choice(letters))
print(*answer)
