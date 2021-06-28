file = open("zen.txt", "r")
row = file.readlines()
row.reverse()
print(''.join(row).strip('\n'))