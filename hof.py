#HOF - higher order functions

L = list(range(1,11))


#map
print("Map stuff")
def square(x):
	return x**2

Lm = []
for i in L:
	Lm.append(square(i))
print(Lm)


#m = list(map(square,L))
#print(m)

m = list(map(lambda x: x**2, L))
print(m)

mc = [x**2 for x in L]
print(mc)


#filter
print("filter stuff")
def greater_than_five(x):
	return x > 5

Lf = []
for i in L:
	if greater_than_five(i):
		Lf.append(i)
print(Lf)

f = list(filter(greater_than_five, L))
print(f)

fc = [x for x in L if x > 5]
print(fc)


#reduce
print("reduce stuff")

s = 0
for i in L:
	s += i
print(s)



