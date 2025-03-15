print("Hello")

a = 7
b = 3.14
c = "mama"
d = True
e = [1,2,3,4,6]
#print(e[1:3])
f = {1:"mama", 2:"papa"}
#print(f[1])
g = (2,3,5,76)
h = {100,13,5,7, 1}
#print(h)

# < > <= >= == != not

def printLine(count=20):
    for i in range(count):
        print("+", end='')
    print()

if a == 5:
    print("a = 5")
else:
    print("a != 5")

printLine()

while a >= 1:
    print(a, end=' ')
    a -= 1
print()

printLine()

for i in e:
    print(i, end=' ')
print()

printLine(40)

