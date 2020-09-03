def recur_factorial(n):
   if n == 1:
       return n
   elif n==0:
       return 1
   elif n<0:
       return 0
   else:
       return n*recur_factorial(n-1)
 num = 7
 print("The factorial of", num, "is", recur_factorial(num))
