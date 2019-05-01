# Code-Quality-Analyzer-
Carried Static code Analysis using Code Quality Metrics like Maintainbility Index, Halstead Metrics and Cyclomatic Complexity.
All the code is written in pyhton and the static analysis is carried on C programs.

# Maintainability Index:
It is a software programming metric which measures how maintable the code is. Here the maintainability refers to the ease of support and change. 
It is calculated as a function of Halstead Metrics, Cyclomatic Comlexity and Lines Of Code.

> **Formula: MI = 171 - 5.2xln(V) - 0.23xG - 16.2xln(LOC)** 
- V = Halstead Volume.
- G = Cyclomatic Complexity.
- LOC = Lines of Code.

# Halstead Metrics:
Developed by Maurice Howard Halstead in 1977.
These are computed statically from the code. The algorithm is completely based on tokens which are generated from the Abstract Syntax Tree (AST) of a C program.
These tokens later are classified into operators and operands in the given code. 
> Operators like: Arithmatic Operaotrs (+, -, *, /), Type identifiers(int, float), Binary Operators(<, >, <=, +=, /=), 
                  Brackets({}, (), []) and Characters(, ; " '), main, for, while, if, else, return, break, struct, union.
> Operands like: Constants(0, 1, 2...) and Variable Names(a, b, c...), Function Declarations(add, any func name...)

The following are the base measures that can be collected as:
- n1: Distinct nuber of operators in a program.
- n2: Distinct nuber of operands in a program.
- N1: Total number of operators in a program.
- N2: Total number of operands in a program.

## Below are the different proposed Halstead Metrics:
- **Program Length :** This is the total number of operator and operand occurances.
> There are different methods propsed for this.
  - $ N = N1 + N2$
  - $ N^ = (n1*\log_2 n1) + (n1*\log_2 n1) $
