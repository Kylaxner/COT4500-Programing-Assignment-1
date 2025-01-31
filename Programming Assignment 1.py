# src/main/assignment_1.py

# Implementation of all four methods

# Method 1: Iterative square root approximation
def iterative_square_root():
    x0 = 1.5
    tol = 0.000001
    iter_count = 0
    diff = x0
    x = x0

    print(f"{iter_count} : {x}")

    while diff >= tol:
        iter_count += 1
        y = x
        x = (x / 2) + (1 / x)
        print(f"{iter_count} : {x}")
        diff = abs(x - y)

    print(f"\nConvergence after {iter_count} iterations")


# Method 2: Bisection method
def bisection_method(f, left, right, tol, max_iter):
    i = 0
    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2
        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p

    print(f"Convergence after {i} iterations.")
    return (left + right) / 2


# Method 3: Fixed-point iteration
def fixed_point_iteration(g, p0, tol, max_iter):
    i = 1
    while i <= max_iter:
        p = g(p0)
        if abs(p - p0) < tol:
            print(f"SUCCESS: Approximation p = {p} after {i} iterations.")
            return p

        i += 1
        p0 = p

    print("FAILURE: Method did not converge within the maximum iterations.")
    return None


# Method 4: Newton's Method
def newtons_method(f, f_prime, p0, tol, max_iter):
    i = 1
    while i <= max_iter:
        if f_prime(p0) == 0:
            print("Unsuccessful: Derivative is zero.")
            return None

        p_next = p0 - f(p0) / f_prime(p0)
        if abs(p_next - p0) < tol:
            print(f"SUCCESS: Approximation p = {p_next} after {i} iterations.")
            return p_next

        i += 1
        p0 = p_next

    print("FAILURE: Method did not converge within the maximum iterations.")
    return None


if __name__ == "__main__":
    # Run all methods as examples
    print("Iterative Square Root Method:")
    iterative_square_root()

    print("\nBisection Method:")
    def sample_function(x):
        return x**2 - 2

    root = bisection_method(sample_function, 1, 2, 0.000001, 100)
    print(f"Approximate root: {root}")

    print("\nFixed-Point Iteration Method:")
    def iterative_function(x):
        return 0.5 * (x + 2 / x)

    fixed_point_iteration(iterative_function, 1.5, 0.000001, 100)

    print("\nNewton's Method:")
    def derivative(x):
        return 2 * x

    root_newton = newtons_method(sample_function, derivative, 1.5, 0.000001, 100)
    print(f"Approximate root: {root_newton}")
