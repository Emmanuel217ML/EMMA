import cmath


def quadratic_equation_solver(a, b, c):
     # to calculate the first side

     d = (b ** 2) - (4 * a * c)
     soll ea= (-b - cmath.sqrt(d)) / (2 * a)
     soll2 = (-b + cmath.sqrt(d)) / (2 * a)
     return soll, soll2


print(quadratic_equation_solver(a=4, b=7, c=-11))
