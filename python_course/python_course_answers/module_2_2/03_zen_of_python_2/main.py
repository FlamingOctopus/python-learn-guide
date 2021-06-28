file = open("zen.txt", 'r')

rows = file.readlines()
letter_count, words_count = 0, 0
for row in rows:
    for sym in row:
        if sym.isalpha():
            letter_count += 1
        if sym.isspace():
            words_count += 1
file.close()
file = open("zen.txt", 'r')

print(f"В файле {len(rows)} строк \n{letter_count} букв\n{len(file.read().split())} слов")
