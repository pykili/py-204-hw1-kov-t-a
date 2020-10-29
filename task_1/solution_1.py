a=input( 'Введите последовательность цифр' )
b = 0
i = 0
for i in a:
  if int(i)>b:
    b=int(i)
print('Самая большая цифра -',b)

