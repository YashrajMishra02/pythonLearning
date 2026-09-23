# Given a decimal number (integer N), convert it into binary and print.

# num = int(input("Enter the integer: "))
# l = []
# ans = 0
# i = 0
# while(num != 0):
#     rem = int(num%2)
#     l.append(rem)
#     num = int(num/2)
# i = len(l)
# while(i != 0):
#     print(l[i-1],end='')
#     i -= 1




num = int(input("Enter the integer: "))
ans = 0
i = 0
while(num != 0):
    rem = int(num%2)
    pv = 10**i
    ans += rem * pv
    num = int(num/2)
    i += 1
print(ans)