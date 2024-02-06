def f(x, y):
    return 2 * x**2 - y

def euler_method(x0, y0, h, x_target):
    x = x0
    y = y0
    while x < x_target:
        y += h * f(x, y)
        x += h
    return y

x0 = 2
y0 = 0
h = 0.1
x_target = 2.2

result = euler_method(x0, y0, h, x_target)
print("Estimation de y(2.2) avec la méthode d'Euler:", result)
