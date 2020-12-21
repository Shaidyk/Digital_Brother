""" Factorial """
n = 1
for i in range(1, 101):
    n = n * i

n = str(n)

""" Plague of all factorial numbers """
sum_factorial = []
for i in n:
    sum_factorial.append(int(i))

print(sum(sum_factorial))
