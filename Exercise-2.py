#Find sum recursively
def recursive_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + recursive_sum(n-1)

#Count digits recursively
def count_digits(n):
    if n == 0:
        return 0
    if n//10 == 0:
        return 1
    return 1 +  count_digits(n//10)

#Reverse a number
from math import log10
def reverse_digits(n):
    if n < 10:
        return n
    else:
        return n%10 * 10 ** int(log10(n//10) + 1) + reverse_digits(n//10)

#Palindrome Strings
def palindrome(input_str):
    return input_str == input_str[::-1]

def max_sub_palindrome(input_str):
    def run(input_str,max):
        if len(input_str) == 0:
            return max
        for i in range(len(input_str)):
            if palindrome(input_str[:i+1]) and len(input_str[:i+1])> len(max):
                max =input_str[:i+1]
        return run(input_str[1:],max)
    max =''
    return run(input_str,max)

#coprimes
def coprime(a, b):
    for i in range(2,a+1):
        if a%i == 0 and b%i == 0:
            return False
    return True
def count_coprimes(n):
    def run(n,i,k):
        if coprime(n,i):
            k +=1
        if i == n:
            return k
        return run(n,i+1,k)
    return run(n,2,1)


