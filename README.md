# Computational Physics & Scientific Computing Journal

[![Language: C](https://img.shields.io/badge/Language-C11-blue.svg)](https://en.wikipedia.org/wiki/C11_(C_standard_revision))
[![Language: Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Aim
The core objective of this repository is to bridge the gap between theoretical physics and computational implementation. By documenting university coursework alongside independent computational explorations, this repository builds an open-access foundational knowledge base for scientific computing. It serves as a structured, reproducible reference translating mathematical physics into clean, executable code.

## Target Audience
* **Physics & Engineering Students:** Seeking a clear, applied introduction to computational methods and numerical analysis.
* **Self-Learners:** Looking for structured, documented examples of scientific libraries and algorithms.
* **Researchers & Theorists:** Transitioning from analytical equations to numerical modeling, discretization, and scientific data visualization.

---

## Scope of the Repository

### 1. The Core Toolkit
* **Languages:** 
  * **C (C11):** Low-level memory management, pointers, explicit array manipulation, and high-performance numerical execution.
  * **Python (3.9+):** Rapid algorithm prototyping, vectorization, modular scripting, and high-level data analysis.
* **Scientific Ecosystem:**
  * **NumPy:** Vectorized array operations, linear algebra, and discrete grid representations.
  * **SciPy:** Advanced optimization, numerical quadrature, interpolation, root-finding, and differential equation solvers.
  * **Pandas:** Structured tabular data manipulation, sensor data cleaning, and CSV file I/O pipelines.
  * **Matplotlib:** Publication-quality 2D/3D plots, vector fields (`quiver`/`streamplot`), and contour maps.
  * **Seaborn:** High-level statistical visualization, distribution density estimation (KDE), and parameter correlation heatmaps.

### 2. Numerical Physics & Methods
* **Root-Finding & Optimization:** Bisection, Secant, and Newton-Raphson methods.
* **Calculus & Finite Differences:** $\mathcal{O}(h)$ vs. $\mathcal{O}(h^2)$ spatial derivatives, discrete grid operators, and numerical integration (Simpson's / Trapezoidal).
* **Ordinary Differential Equations (ODEs):** Euler, Runge-Kutta 4th Order (RK4), and symplectic Velocity Verlet integration (Harmonic Oscillator, planetary orbits).
* **Linear Algebra & PDEs:** Direct ($LU$) and iterative (Jacobi, Gauss-Seidel) solvers, eigenvalue state calculations (Lanczos/QR), 1D Heat Equation (FTCS vs. Crank-Nicolson), and 2D Laplace relaxation.
* **Stochastic & Monte Carlo Methods:** 1D and 2D random walks (verifying $\langle r^2(t) \rangle \propto t$), importance sampling, and Metropolis-Hastings Markov Chain Monte Carlo (MCMC).

---

## Repository Structure

```text
.
├── basic_C/
│   ├── 01_syntax_and_types/     # Variables, data types, I/O, and operators
│   ├── 02_control_flow/         # Conditionals, switch-case, loops, break/continue
│   ├── 03_functions_and_scope/  # Function prototypes, pass-by-value, variable scope
│   ├── 04_arrays_and_strings/   # 1D/2D arrays, matrix operations, C-strings
│   ├── 05_pointers_and_memory/  # Pointers, pass-by-reference, dynamic memory (malloc/free)
│   └── Makefile                 # Automated build script for all C programs
│
├── basic_python/
│   ├── lecture_01/              # Fundamentals, syntax, and basic I/O
│   ├── lecture_02/              # Data types, operators, and control structures
│   ├── lecture_03/              # Functions, recursion, and modular design
│   ├── lecture_04/              # Data structures (lists, tuples, dicts, sets)
│   ├── lecture_05/              # File handling and error management
│   └── problems/                # Practice exercises and problem sets
│
├── python_libraries/
│   ├── 01_numpy/                # Vectorized arrays, linear algebra, and random sampling
│   ├── 02_pandas/               # Series, DataFrames, indexing, cleaning, and file I/O
│   ├── 03_scipy/                # Quadrature, optimization, curve fitting, splines, ODEs
│   ├── 04_matplotlib/           # 2D/3D plots, subplots, vector fields, and heatmaps
│   └── 05_seaborn/              # Statistical distributions, correlation heatmaps, pairplots
│
├── computational_physics/
│   ├── 01_roots_polynomial/     # Bisection, Newton-Raphson, and Secant methods
│   ├── 02_interpolation/        # Polynomial and cubic spline interpolation
│   ├── 03_numerical_calculus/   # Finite difference derivatives and numerical integration
│   ├── 04_ODE/                  # Euler, Velocity Verlet, and RK4 integrators
│   ├── 05_linear_algebra/       # Direct (LU) and iterative (Jacobi, Gauss-Seidel) solvers
│   ├── 06_PDE/                  # 1D Heat equation (FTCS/Crank-Nicolson) & 2D Laplace
│   └── 07_Monte_Carlo/          # Random walks (MSD scaling), importance sampling, MCMC
│
├── .gitignore                   # Ignores build binaries, caches, and output datasets
├── LICENSE                      # Open-source license (MIT)
└── README.md                    # Project documentation
