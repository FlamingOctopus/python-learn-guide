from collections import OrderedDict

with open("text.txt", 'r') as file:
    file = file.readlines()
    count = 0
    syms_dict = {}
    for row in file:
        for sym in row:
            if sym.isalpha() and sym.isascii():
                sym = sym.lower()
                if sym in syms_dict:
                    syms_dict[sym] += 1
                else:
                    syms_dict[sym] = 1
                count += 1

syms_dict = OrderedDict(sorted(syms_dict.items(), key=(lambda x: x[0])))
syms_dict = sorted(syms_dict.items(), key=lambda x: x[1], reverse=True)

f = open("analysis.txt", 'w')
for item in syms_dict:
    f.write(f"{item[0]} {round(int(item[1]) / count, 3)}")
    f.write("\n")
f.close()
