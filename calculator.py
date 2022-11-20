n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))

print("Operators List:\n1. +\n2. -\n3. *\n4. /\n5. %")

op=input("Enter one of the operators mentioned in the above list : ")

if (op=='+'):
  print(n1,'+',n2,'=',n1+n2)

elif (op=='-'):
  print(n1,'-',n2,'=',n1-n2)

elif (op=='*'):
  print(n1,'*',n2,'=',n1*n2)

elif (op=='-'):
  print(n1,'-',n2,'=',n1-n2)

elif (op=='/'):
  if (n2!=0):
    print(n1,'/',n2,'=',n1/n2)
  else:
    print("We cannot divide a number by 0")

elif (op=='%'):
  if (n2!=0):
    print(n1,'%',n2,'=',n1%n2)
  else:
    print("We cannot divide a number by 0")

else:
  print('Invalid choice')
