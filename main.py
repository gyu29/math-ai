import sympy
import re

class WordProblemSolver:
    def __init__(self):
        # Define symbols for variables in the problem
        self.x, self.y, self.z = sympy.symbols('x y z')

        # Define additional constants if needed
        self.pi = sympy.pi
        self.e = sympy.E

        # Define other functions like sqrt, sin, cos, tan, log, etc.
        self.sqrt = sympy.sqrt
        self.sin = sympy.sin
        self.cos = sympy.cos
        self.tan = sympy.tan
        self.log = sympy.log

    def solve_complex_word_problem(self, problem):
        # Define a pattern to match mathematical expressions in the problem
        pattern = r'(\w+)\(([\w\s\*\/\-\+\^]+)\)'
        matches = re.findall(pattern, problem)

        # Replace text-based mathematical expressions with symbolic math
        for match in matches:
            function, expr = match
            problem = problem.replace(f"{function}({expr})", f"{function}({expr})")

        # Parse the word problem using sympy
        parsed_problem = sympy.sympify(problem)

        # Solve the problem symbolically
        solution = sympy.solve(parsed_problem, self.x)

        # Display and return the symbolic solution
        print(f"Symbolic Solution: {solution}")
        return solution

# Example usage:
solver = WordProblemSolver()
problem = "Solve the equation: sqrt(x) + 2*sin(x) - log(x) = 3"
solution = solver.solve_complex_word_problem(problem)
