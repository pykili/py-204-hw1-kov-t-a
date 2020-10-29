inp = str(input())
mfchar = str()
mfcount = 0
for char in inp:
  if inp.count(char) > mfcount:
    mfchar = char
    mfcount = inp.count(char)
print(mfchar)
