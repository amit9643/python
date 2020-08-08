# 1.	Write a python program that finds the second largest number from a given list of numbers.
#
# Examples:
# Input : list_1 = [15, 23, 9]
# Output: 15
#
# Input : list_2 = [79, 13, 29, 7, 200]
# Output: 79
#
# Solution

input = list(map(int,input().strip().split()))
mx = max(input[0], input[1])
secondmax = min(input[0], input[1])
n = len(input)
for i in range(2, n):
   if input[i] > mx:
       secondmax = mx
       mx = input[i]
   elif input[i] > secondmax and mx != input[i]:
       secondmax = input[i]
   else:
       if secondmax == mx:
           secondmax = input[i]

print(str(secondmax))

