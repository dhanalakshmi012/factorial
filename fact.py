# factorial
num=raw_input("enter the num:")
factorial=1
if num<0:
   print("enter positive num")
elif num==0:
   print("fact=1")
else:
   for i in range(1,num+1):
      factorial=factorial*i
      print("factorail",factorial)
