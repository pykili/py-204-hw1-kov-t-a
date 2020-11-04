n=0
while n<=10:
    a=input()
form = str()
lemma = str()
if a[0] != '\t' and a[0] != " " and form[1] != "lemma":
  while a[1]!=int:
    n=n+1
  while a[2]!='\t':
    n=n+1
  while a[4]!='\t':
    n=n+1
  while a[6]!='\t':
    n=n+1
  while a[form]!='\t':
     form=form+1
  while a[lemma]!='\t':
      lemma=lemma+1
if lemma!=form:
  print(form, lemma)
  
