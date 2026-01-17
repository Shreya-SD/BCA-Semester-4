s1={1,2,3,4,5}
print("elements of set1 are:",s1)
print("number of elements are:",len(s1))
print("maximum value:",max(s1))
print("minimum value:",min(s1))
print("sum:",sum(s1))
print("sorted list:",sorted(s1))
print("any set:",any(s1))
print("all set:",all(s1))
s1.add(15)
print("after adding:",s1)

s2={2,4,6,8,10}
print("elements of set2 are:",s2)
s2.pop()
print("after pop:",s2)

s3={3,6,9,12,15}
print("elements of set3 are:",s3)
print("elements in both sets are:",s2.union(s3))
print("common elements are:",s2.intersection(s3))
print("difference:",s2.difference(s3))

s4={1,2}
s5={1,2,3}
print("subset result:",s4.issubset(s5))

s6={3,8,2,6}
s7={4,7,1,9}
print("disjoint result:",s6.isdisjoint(s7))

s8={3,8,4,6}
s9={3,8}
print("superset result:",s8.issuperset(s9))
