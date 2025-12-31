def isLeapYear(year):
  if(year % 4 ==0 and year %100!=0) or year %400==0:
    return True
  else:
    return False

year=int(input('Enter the Year))

if isLeapYear(year):
     print (f'{year} is a leap year.')
else:
     print (f'{year} is not a leap year.')
