print("---enter employee details---")
empcode=int(input("empcode:"))
name=input("name:")
dept=input("dept:")
designation=input("designation:")
basic=float(input("enter basic salary:"))
hra=basic*0.10
da=basic*0.05
pf=basic*0.12
netsalary=(basic+hra+da)-pf
print("----salary card----")
print('*'*35)
print(f"empcode        :{empcode}")
print(f"name           :{name}")
print(f"dept           :{dept}")
print(f"designation    :{designation}")
print('-'*35)
print(f"salary         :{basic:,.2f}")
print(f"HRA            :{hra:,.2f}")
print(f"DA             :{da:,.2f}")
print(f"PF             :{pf:,.2f}")
print('-'*35)
print(f"netsalary      :{netsalary:,.2f}")
print('*'*35)
