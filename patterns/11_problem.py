# Program to print double hill pattern
'''
   *       *
  * *     * * 
 * * *   * * * 
* * * * * * * *
'''

num =  int(input("Enter no of rows for double hill pattern: "))
i = 1
while(i <= num):
    print(" " * (num - i), end='')
    print("* " * i, end='')
    print(" " * (num * 2 - 2 * i), end='')
    print("* " * i, end='')
    print()
    i += 1
