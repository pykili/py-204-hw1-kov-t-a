a = input('Введите последовательность букв')
alphabet = str()
i=0
for i in a:
    if i not in alphabet:
        alphabet = alphabet + i
print(alphabet)
