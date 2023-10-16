# Complex Equation Solver with Word Problems

This Python class provides a solution for solving complex equations within word problems using the `sympy` library. It allows you to handle equations involving variables, constants like pi and e, and mathematical functions like sqrt, sin, cos, tan, log, and more.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Solving complex equations within word problems can be challenging. This class simplifies the process by providing a framework for symbolic mathematics and textual understanding. It uses the `sympy` library to handle equations and mathematical expressions within word problems.

## Features

- Symbolically solve equations with variables and constants.
- Recognize and replace text-based mathematical expressions with symbolic math.
- Handle mathematical functions like sqrt, sin, cos, tan, log, pi, and e.

## Installation

1. Clone this repository:

   ```bash
   https://github.com/gyu29/math-ai

2. Navigate to the project directory:
   cd mathai

## Usage 
   ```python```
   
      from complex_equation_solver import WordProblemSolver  

      solver = WordProblemSolver()  

      problem = "Solve the equation: sqrt(x) + 2*sin(x) - log(x) = 3"  
      solution = solver.solve_complex_word_problem(problem) 

The solve_complex_word_problem method can be used to solve complex equations within word problems. Customize the method for your specific problem requirements.  

## Contributing  
Contributions to this project are welcome. To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and submit a pull request.

## License  
This project is licensed under the MIT License - see the LICENSE file for details.
