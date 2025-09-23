import math

# -----------------------------
# Numerical Integration Methods
# -----------------------------

# 🟢 Trapezoidal Rule
# Formula: I ≈ (h/2) [ f(x0) + 2(f(x1)+...+f(xn-1)) + f(xn) ]
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        result += 2 * f(a + i * h)
    return (h / 2) * result


# 🟢 Simpson’s 1/3 Rule
# Formula: I ≈ (h/3) [ f(x0) + 4(f(x1)+f(x3)+...) + 2(f(x2)+f(x4)+...) + f(xn) ]
# Condition: n must be EVEN
def simpson_one_third_rule(f, a, b, n):
    if n % 2 != 0:
        return "❌ Simpson’s 1/3 Rule requires even intervals"
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 4 * f(a + i * h)
    return (h / 3) * result


# 🟢 Simpson’s 3/8 Rule
# Formula: I ≈ (3h/8) [ f(x0) + 3(f(x1)+f(x2)+f(x4)+...) + 2(f(x3)+f(x6)+...) + f(xn) ]
# Condition: n must be MULTIPLE OF 3
def simpson_three_eighth_rule(f, a, b, n):
    if n % 3 != 0:
        return "❌ Simpson’s 3/8 Rule requires n multiple of 3"
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 3 * f(a + i * h)
    return (3 * h / 8) * result


# -----------------------------
# User Input Section
# -----------------------------
print("🔹 Numerical Integration Calculator 🔹")
print("👉 Enter function f(x) using 'x' (e.g., x**2, math.sin(x), math.exp(x))\n")

expr = input("Enter function f(x): ")   # example: x**2
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of intervals n: "))

# Function from user input
def f(x):
    return eval(expr, {"x": x, "math": math})

# -----------------------------
# Show Results
# -----------------------------
print("\n✅ Results:")
print("---------------------------")
print(f"Trapezoidal Rule   = {trapezoidal_rule(f, a, b, n)}")
print(f"Simpson's 1/3 Rule = {simpson_one_third_rule(f, a, b, n)}")
print(f"Simpson's 3/8 Rule = {simpson_three_eighth_rule(f, a, b, n)}")
print("---------------------------")
