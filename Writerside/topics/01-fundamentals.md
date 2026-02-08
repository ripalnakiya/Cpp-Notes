# Fundamentals
<show-structure depth="2"/>

## Compiler vs Interpreter

| Compiler                                                                                                              | Interpreter                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Translates the entire source code into machine code **at once**, producing a separate executable file (e.g., `.exe`). | Translates and executes the source code **line by line** without generating a separate executable file. |
| Compilation happens only once. After that, the program can run **without the compiler**.                              | Translation happens **every time** the program is run, so an interpreter is required each time.         |
| Compiled programs generally execute **faster** because they run directly on the machine.                              | Interpreted programs are usually **slower** because execution happens within the interpreter.           |

## Programming Paradigms

1. Monolithic Programming
    - The entire program is written as a single, large block of code, often in one file, with little or no separation of concerns.
2. Procedural / Modular / Functional Programming
    - The program is divided into smaller, reusable functions or modules that perform specific tasks.
    - Example: C language primarily follows the procedural programming paradigm.
3. Object-Oriented Programming (OOP)
    - The program is organized around objects and classes that encapsulate data and behavior.
    - Example: C++ supports object-oriented programming.

> C++ is multi-paradigm. It supports procedural, object-oriented, and even functional styles.
{style="note"}

## Header File

- Contains declarations of functions, classes, macros, and constants.
- Does not contain executable code (usually).
- Used by the compiler during compilation.
- They're included using `#include`

```c++
#include <iostream>
```

`iostream` tells the compiler: “Relax, `cout` exists. I’ll show you the body later.”

## Library File

- Contains the definitions / implementations of functions and classes.
- Provides the actual compiled code.
- Used during linking.
- Can be:
  - Static library (`.a`, `.lib`)
  - Dynamic library (`.so`, `.dll`)

Example:
`libstdc++.so` → contains the real implementation of `cout`.

## Namespace

**Problem:**

```c++
void fun() {
    cout << "First" << endl;
}

void fun() {
    cout << "Second" << endl;
}

int main() {
    fun();
}
```

Program will generate error, mentioning `fun()` is redefined.

**Solution:**

```c++
namespace first
{
    void fun() {
        cout << "First" << endl;
    }
};

namespace second
{
    void fun() {
        cout << "Second" << endl;
    }
};

int main()
{
    fun();          // Invalid Statement, we'll need scope resolution
    first::fun();   // First
    second::fun();  // Second
}

```

```c++
namespace first
{
    void fun() {
        cout << "First" << endl;
    }
};

namespace second
{
    void fun() {
        cout << "Second" << endl;
    }
};

using namespace first;
void main()
{
    fun();          // First - Valid Statement
    first::fun();   // First
    second::fun();  // Second
}
```

### Namespace Summary

A namespace is a named scope that
groups identifiers like variables, functions, and classes
to avoid name collisions.

```c++
namespace math {
    int add(int a, int b) {
        return a + b;
    }
}
```

> Namespaces prevent name collisions
{style="note"}

```c++
std::sort
mylib::sort
```
