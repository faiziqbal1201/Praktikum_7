import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))
result_a = a(10)
result_b = b(3, 4)
result_c = c(1, 2, 3, 4, 5)
result_d = d("Hai")

print(result_a)
print(result_b)
print(result_c)
print(result_d)