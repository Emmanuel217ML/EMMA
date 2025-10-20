import math

def quad(a,b,c):
    upper_side = (b ** 2)
    first = (4 * a * c)

    h = upper_side - first
    emm = (-b - math.sqrt(h)) / (2 * a)
    enn = (-b + math.sqrt(h)) / (2 * a)

    return (enn, emm)

print(quad(1,b=5,c=6))


