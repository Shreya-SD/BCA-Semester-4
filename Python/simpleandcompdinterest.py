p=float(input("enter principal amount:"))
r=float(input("enter rate of interest(in %):"))
t=float(input("enter time period(in years):"))
n=float(input("enter no. of times interest is compounded per year:"))
SI=(p*r*t)/100
total_amt=p*(1+(r/(100*n)))**(n*t)
CI=total_amt-p
print("simple interest:",round(SI,2))
print("compound interest:",round(CI,2))
