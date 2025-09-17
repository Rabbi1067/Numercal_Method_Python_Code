def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# ---- User Input ----
n = int(input("How many points? "))

x_points = []
y_points = []

for i in range(n):
    x_val = float(input(f"Enter x{i+1}: "))
    y_val = float(input(f"Enter y{i+1}: "))
    x_points.append(x_val)
    y_points.append(y_val)

x = float(input("Enter x to interpolate: "))

# ---- Calculation ----
y = lagrange_interpolation(x_points, y_points, x)

print(f"For x = {x}, interpolated y = {y}")
