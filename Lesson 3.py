import math
import random


def summ(a, b):
    c = a + b
    return c
    print("End func")

# a1 = 5
# a2 = 7
#
# res = summ(100, 200)
# print(res)


# a = 5
# print(a)

def func():
    global a
    a = 10


# func()
# print(a)

def isEven(a):
    return a % 2 == 0


# numbers = [random.randint(1, 100) for i in range(20)]
# print(numbers)

# count = 0
# for n in numbers:
#     if isEven(n):
#         count += 1

# print(count)

# print("Корінь з 25 = ", math.sqrt(25))


def game(user_choice):
    comp_choice = random.choice("KNB")
    user_choice = str.upper(user_choice)
    print(f"Гравець - {user_choice}, Комп'ютер - {comp_choice}")
    if user_choice == comp_choice:
        return "D"
    elif (user_choice == "K" and comp_choice == "N" or
          user_choice == "N" and comp_choice == "B" or
          user_choice == "B" and comp_choice == "K"):
        return "U"
    else:
        return "C"


def print_result(winner, result):
    if winner == "D":
        print("В цьому раунді нічья")
    elif winner == "U":
        print("В цьому раунді переміг гравець")
        result["user"] += 1
    elif winner == "C":
        print("В цьому раунді переміг комп'ютер")
        result["comp"] += 1
    print(f"Гравець - {result["user"]}, комп'ютер - {result["comp"]}")


result = {"user" : 0, "comp" : 0}

for i in range(1, 4):
    print(f" ====== РАУНД №{i} ======")
    print_result(game(input("Виберіть K, N, B - ")), result)
    print()

