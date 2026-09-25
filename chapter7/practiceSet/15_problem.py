# program to print nth fibonacci series
n = int(input("enter the number to find nth fibonnaci series: "))
base1 = 0
base2 = 1
i= 0
while(i < n):
    ans = base1 + base2
    base1 = base2
    base2 = ans
    i+=1
print(ans)