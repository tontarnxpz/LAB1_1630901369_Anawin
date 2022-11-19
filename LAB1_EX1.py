x = int(input('Enter your number : '))
k = x
y = 0
i = 1
j = 0
spc = x//2
for i in range(1,x+1,i+1):
   print(" "*spc,"*"*i)
   spc -= 1

for j in range(k-2,0,j-2):
   print(" "*(spc+2),"*"*j)
   spc += 1