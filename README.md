
# Code Quality Analyzer
Carried Static code Analysis using Code Quality Metrics like Maintainability Index, Halstead Metrics and Cyclomatic Complexity.
All the code is written in python and the static analysis is tested on C programs.

# Maintainability Index:
It is a software programming metric which measures how maintainable the code is. Here the maintainability refers to the ease of support and change. 
It is calculated as a function of Halstead Metrics, Cyclomatic Complexity and Lines Of Code.

> **Formula: MI = 171 - 5.2xln(V) - 0.23xG - 16.2xln(LOC)** 
- V = Halstead Volume.
- G = Cyclomatic Complexity.
- LOC = Lines of Code.

# Halstead Metrics:
Developed by Maurice Howard Halstead in 1977.
These are computed statically from the code. The algorithm is completely based on tokens which are generated from the Abstract Syntax Tree (AST) of a C program.
These tokens later are classified into operators and operands in the given code. 
> Operators like: Arithmetic Operators (+, -, *, /), Type identifiers(int, float), Binary Operators(<, >, <=, +=, /=), Brackets({}, (), []) and Characters(, ; " '), main, for, while, if, else, return, break, struct, union.
> 
> Operands like: Constants(0, 1, 2...) and Variable Names(a, b, c...), Function Declarations(add, sub, any func name...)

The following are the base measures that can be collected as:
- n1: Distinct number of operators in a program.
- n2: Distinct number of operands in a program.
- N1: Total number of operators in a program.
- N2: Total number of operands in a program.

## Below are the different proposed Halstead Metrics:
- **Program Length :** This is the total number of operator and operand occurrences.
There are different methods proposed to calculate Program Length.
  - $N = N1 + N2$
  - $N\_ = (n1*\log_2 n1) + (n1*\log_2 n1)$
  - $N_j = log_2(n1!) + log_2(n2!)$
  - $N_b = (n1*\log_2 n2) + (n2*\log_2 n1)$
  - $N_c = (n1*\sqrt n1) + (n2*\sqrt n2)$
  - $N_s = \frac{(n1+n2)*log_2 (n1+n2)}{2}$
 
 - **Program Vocabulary:** The total number of unique operator and unique operand occurrences.
	  - $n = n1 + n2$
  - **Program Volume:** It proportional to the size of the program. The unit of measurement of program volume is "bits". If a uniform binary encoding is used, then it is the actual size of a program.
	  - $V = N * log_2 (n)$
  - **Program Difficulty:** Programming practices such as redundant usage of operands, or the failure to use higher-level control constructs will tend to increase the volume as well as the difficulty.
	  - $D = (n1/2) * (N2/2)$
  - **Program Level:** It describes the level of abstraction provided by the programming Language.
	- $L = 1/D$
- **Programming Effort:** Effort required implementing or understanding the program is directly proportional to difficulty and volume.
	- $E = D * V$
- **Intelligence Content:** Determines the amount of intelligence presented (stated) in the program.
	- $I = V/D$
- **Programming Time:** The time needed to translate our algorithm into coding in a specified language.
	- $T = E/(f*S)$

# Cyclomatic Complexity:
It is a quantitative approach to measure the complexity of code.
Cyclomatic complexity gives the number of independent paths in the CFG of the program.

# Entropy:
Code quality measure to understand how repetitive the code is.
The Shannon entropy equation provides a way to estimate the average minimum number of bits needed to encode a string of symbols, based on the frequency of the symbols.
> $H(X) = -\Sigma p_i \log_2 p_i$

Extending Shannon entropy technique to work on Abstract syntax tree. In this case, overlapping segments of the tree are considered. Swap strings of Shannon entropy with sub-trees of the AST.
