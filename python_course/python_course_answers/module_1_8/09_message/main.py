string = input("Сообщение:").split()
new_string = [word[::-1] if word[-1].isalpha() else word[-2::-1] + word[-1] for word in string]

print(" ".join(new_string))