string = input("Введите строку: ")
left = string[:string.find('h')]
middle = string[string.find('h'):string.rfind('h') + 1]
right = string[string.rfind('h') + 1:]
string = left + middle[::-1] + right
print(string)