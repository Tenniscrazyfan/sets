id = {1,1,1,2,3,7,5,6,7}
print (id)
id.add(4)
print(id)

marks = [56,87,6,7,3,4,5,6]
id.update(marks)
print(id)
id.discard(56)
print(id)

print(max(id))
print(min(id))
print(sum(id))
print(sorted(id))

seta = {5,6,4,7,8,90}
setb = {5,6,7,3,4,23,4,5,1}
print(seta.union(setb))
print(seta.intersection(setb))
print(seta.difference(setb))
print(setb.difference(seta))