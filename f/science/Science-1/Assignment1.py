import math, random
import matplotlib.pyplot as pypl

s = 7500
n = 750
probability = []
calc = []
for i in range(n):
    probability.append(0)
for i in range(s):
    first_disp = 0
    second_disp = 0
    for j in range(n):
        p = random.random()
        if(p > 0.5):
            first_disp = first_disp + 1
        else:
            first_disp = first_disp - 1
        p = random.random()
        if(p > 0.5):
            second_disp = second_disp + 1
        else:
            second_disp = second_disp - 1
        if first_disp == second_disp:
            probability[j] = probability[j] + 1
for i in range(n):
    probability[i] = probability[i]/s
    n_factorial = math.factorial(i + 1)
    n_factorial_2 = math.factorial(2 * i + 2)
    calc.append(n_factorial_2/pow(pow(2, i+1) * n_factorial, 2))

print(calc)
pypl.plot(calc)
pypl.plot(probability)
pypl.show()
