num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   dig = temp % 10
   sum = sum+ dig ** 3
   temp = temp//10
if num == sum:
   print("Armstrong")
else:
   print("not Armstrong number")