#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
#convert number into binary
    binary = bin(n)[2:]
#find the consecutive 1's in the result
    print(type(binary), binary)
#print no. of 1's
    list_1 = binary.split("0")
#110111 .split(0) 
    count_lis = []
    for i in list_1:
        count_lis.append(len(i))
    print(count_lis)
    print(max(count_lis))


    #     #!/bin/python3
    # import sys, math

    # n = int(input().strip())
    # count = 0
    # maxi = 0
    # while n > 0:
    #     if n % 2 == 1:
    #         count += 1
    #     else:
    #         if count > maxi:

    #             maxi = count
    #         count = 0
    #     n=math.floor(n / 2)
    # if count > maxi:
    #     maxi = count
    # print(maxi)
    


#     #!/bin/python3

# import sys
# def binary(n):
#     bin=[]
#     while n>1:        
#         bin.append(n%2)
#         n=n//2
#         if n==0 or n==1:
#             bin.append(n)
#     return bin

# n = int(input().strip())
# bin=binary(n)
# re=0
# result=[]
# for i in range(len(bin)):
#     if bin[i]==1:
#         re=re+1
#     else:
#         result.append(re)
#         re=0
# result.append(re)
# for i in range(len(result)-1):
#     if result[i]>result[i+1]:
#         result[i+1]=result[i]
# print(result.pop())