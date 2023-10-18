#1.1 Implement a function to calculate The factorial of a given numper
def fact_rec(n):
    if n==0 or n==1:
        return 1
    else:
      return n*fact_rec(n-1)
number=int(input("Enter a value:"))
res=fact_rec(number)
print("The factorail of {} is{}".format(number,res))
  
