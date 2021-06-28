import string


def cesar_cipher(alphabet, shift, word):
    res = []
    len_alphabet = len(alphabet)
    for sym in word:
        if sym == "\n":
            continue
        res.append(alphabet[(alphabet.find(sym) + shift) % len_alphabet])
    return "".join(res)


alphabet = string.ascii_letters
count = 1

rows = open("text.txt")
print("Содержимое файла text.txt:")
for row in rows:
    print(row, end='')
rows.close()

rows = open("text.txt")
file_ciphered = open("cipher_text.txt", 'w')
lines = rows.readlines()
for line in lines:
    file_ciphered.write((cesar_cipher(alphabet, count, line)) + "\n")
    count += 1
file_ciphered.close()

file = open("cipher_text.txt", 'r')
print("\nСодержимое файла cipher_text.txt:")
for word in file:
    print(word, end='')
