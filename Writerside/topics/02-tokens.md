# Tokens

A token is the smallest individual element in a C++ program that has meaning to the compiler.

Example:
```c++
int sum = a + b;
```

Tokens here are:
```python
int | sum | = | a | + | b | ;
```
## Types of Tokens

**1. Keywords**

Reserved words with predefined meaning.

```c++
int, float, if, else, for, while, return, class, namespace
```

We can’t use these as variable names.

**2. Identifiers**

Names given by the programmer to variables, functions, classes, etc.

```c++
sum, totalMarks, calculateSalary
```

Rules:
- Must start with a letter or `_`
- Can contain letters, digits, `_`
- Cannot be a keyword

**3. Literals (Constants)**

Fixed values that do not change during program execution.

```c++
10        // integer literal
3.14      // floating literal
'A'       // character literal
"Hello"   // string literal
true      // boolean literal
```

**4. Operators**

Symbols that perform operations on operands.

```c++
+, -, *, /, %, =, ==, <, >, &&, ||
```

**5. Punctuators / Separators (Special Symbols)**

Characters used to structure the program.

```c++
;  ,  {}  ()  []  ::
```
