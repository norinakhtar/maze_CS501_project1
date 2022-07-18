# def reverse(num:int):

#     reversednum=0
#     while num!=0:
#         digit = num%10
#         reversednum =reversednum*10+digit
#         num //= 10
#     return reversednum


# print(reverse(1234))

def count(n):
    c=0
    while n!=0:
        n=n //10
        c = c+1
    return c
    

print(count(10088))