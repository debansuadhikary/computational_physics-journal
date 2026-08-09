import math
from typing import Callable, Tuple, List, Dict, Any


def secant_method(
    func: Callable[[float], float],
    x0: float,
    x1: float,
    tol: float = 1e-8,
    max_iter: int = 100,
) -> Dict[str, Any]:
    """Finds a root of f(x) = 0 using the Secant Method.

    Parameters:
        func (Callable[[float], float]): Continuous target function f(x).
        x0 (float): First initial guess.
        x1 (float): Second initial guess.
        tol (float): Absolute tolerance for convergence (|x_{n+1} - x_n|).
        max_iter (int): Maximum number of iterations before failure.

    Returns:
        dict: A dictionary containing:
            - 'root' (float): The estimated root value.
            - 'iterations' (int): Total iterations performed.
            - 'converged' (bool): True if target tolerance was met.
            - 'history' (List[Tuple[int, float, float]]): Step history (iter, x_n, f(x_n)).

    Raises:
        ValueError: If f(x1) - f(x0) becomes zero (division by zero).
    """
    history: List[Tuple[int, float, float]] = []

    f_x0 = func(x0)
    f_x1 = func(x1)

    history.append((0, x0, f_x0))
    history.append((1, x1, f_x1))

    for iteration in range(2, max_iter + 1):
        denominator = f_x1 - f_x0

        if math.isclose(denominator, 0.0, abs_tol=1e-15):
            raise ValueError(
                f"Division by zero encountered at iteration {iteration}: "
                f"f({x1}) - f({x0}) ≈ 0."
            )

        # Secant update formula
        x_next = x1 - f_x1 * (x1 - x0) / denominator
        f_next = func(x_next)

        history.append((iteration, x_next, f_next))

        # Convergence check
        if abs(x_next - x1) < tol:
            return {
                "root": x_next,
                "iterations": iteration,
                "converged": True,
                "history": history,
            }

        # Shift variables for next step
        x0, f_x0 = x1, f_x1
        x1, f_x1 = x_next, f_next

    return {
        "root": x1,
        "iterations": max_iter,
        "converged": False,
        "history": history,
    }

if __name__ == "__main__":

    # Physical Example: Finding root of f(x) = x^3 - 2x - 5
    def physical_system(x: float) -> float:
        return x**3 - 2 * x - 5

    # Initial guesses
    guess_a, guess_b = 1.0, 3.0

    result = secant_method(physical_system, x0=guess_a, x1=guess_b, tol=1e-10)

    print("Secant Method Results : ")
    print(f"Converged : {result['converged']}")
    print(f"Root      : {result['root']:.10f}")
    print(f"Iterations: {result['iterations']}")
    print("\nIteration History:")
    print(f"{'Iter':<6} | {'x_n':<16} | {'f(x_n)':<16}")
    print("-" * 44)
    for step, val, f_val in result["history"]:
        print(f"{step:<6} | {val:<16.10f} | {f_val:<16.10e}")
