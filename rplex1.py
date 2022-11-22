import math

def solve_quadratic(a, b, c):
    d = (b ** 2) - 4 * a * c
    s1 = (-b + math.sqrt(d)) / (2 * a)
    s2 = (-b - math.sqrt(d)) / (2 * a)
    return s1, s2

if __name__ == "__main__":
    a = float(input("a: ")) 
    b = float(input("b: "))
    c = float(input("c: "))
    try:
        print(solve_quadratic(a, b, c))
    except:
        print("No real solutions")