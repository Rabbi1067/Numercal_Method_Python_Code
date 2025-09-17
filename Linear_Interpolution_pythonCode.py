def linear_interpolation(x0, y0, x1, y1, x):
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

# User Input
x0 = float(input("Enter first point x0: "))
y0 = float(input("Enter first point y0: "))
x1 = float(input("Enter second point x1: "))
y1 = float(input("Enter second point y1: "))
x  = float(input("Enter the x value to find y: "))

# Result
y = linear_interpolation(x0, y0, x1, y1, x)
print(f"For x = {x}, interpolated y = {y}")
