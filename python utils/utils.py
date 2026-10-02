# Day 1 code : prime sieve (Sieve of Eratosthenes) i.e. Write down all integers from 2 up to your chosen limit \(n\)

def prime_sieve(number):
    s = set()

    for i in range(2, number):
        for j in range(2, i+1):
            if(i==j):
                s.add(i)
                continue
            elif(i%j!=0):
                continue
            elif(i%j==0):
                break
    return s

