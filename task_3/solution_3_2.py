alphabet = str()
i=0
for i in range(10):
  a = input('Введите последовательность букв')
  for i in a:
      if i not in alphabet:
        alphabet = alphabet + i
print(alphabet)
