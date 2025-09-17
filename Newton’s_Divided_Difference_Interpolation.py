# Function to calculate divided difference coefficients
def divided_diff(x_points, y_points):
    n = len(y_points)
    coef = y_points.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x_points[i] - x_points[i-j])
    return coef

# Function to evaluate Newton polynomial at given x
def newton_interpolation(x_points, coef, x):
    n = len(coef)
    result = coef[n-1]
    for i in range(n-2, -1, -1):
        result = result * (x - x_points[i]) + coef[i]
    return result

# -------- User Input --------
n = int(input("How many points? "))

x_points = []
y_points = []

for i in range(n):
    x_val = float(input(f"Enter x{i+1}: "))
    y_val = float(input(f"Enter y{i+1}: "))
    x_points.append(x_val)
    y_points.append(y_val)

x = float(input("Enter x to interpolate: "))

# -------- Calculation --------
coef = divided_diff(x_points, y_points)
y = newton_interpolation(x_points, coef, x)

print(f"Interpolated value at x = {x} is y = {y}")
