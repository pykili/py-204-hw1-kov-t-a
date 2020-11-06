a = input("Введите строку")
is_palindrom = str()
i=0
for i in a:
  is_palindrom=i+is_palindrom
if a==is_palindrom:
 print(True)
else:
  print(False)
