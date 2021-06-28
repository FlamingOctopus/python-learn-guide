file = open('number.txt', 'r')
sum = 0
for row in file:
    for sym in row:
        if sym.isdigit():
            sum += int(sym)
print(sum)
