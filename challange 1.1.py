def fact_rec(n):
  ans=1
  for i in rane(1,n+1):
    ans=ans*i
  return ans
  
number=int(input('Enter your number'))
res = fact_rec(number)

print(f'The factorial of {number} is {res})
