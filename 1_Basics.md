# Table of Contents

[1. Basics](#basics)

[2. Arrays](#arrays)

[3. Pointers](#pointers)

[4. Functions](#functions)

# Basics

## Theory

### Compiler vs Interpreter

- Compilation of source code is done only once
- Compiler generates a separate executable(.exe) file
- Translation of source code to machine code is done only once, so we don't compiler to excute our program.
- The compiled program are fast because they gets executed independently.
- Language is easy (program doesn't executes if there's single error)

- It translates the source code into machine code line by line, and then excutes the line
- We need browser/Interpreter every time we want to run the code. (Translation happens every time we want to run the code)
- Interpreted programs are slow because they get executed inside the interpreter
- Language is difficult (program executes until the error is encountered)

### Programming Paradigm

- Monolothic Programming (single file - entire program)
- Procedural/Modular/Functional Programming (Breaking the program into functions : C language)
- Object Oriented Programming (C++ language)

---

## Basic Concepts

### Datatypes

- Int data type range (Assuming 2 bytes)
  bits : 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

  MSB is used to represent sign of the number
  0 for positive, 1 for negative

  we're remaining with 15 bits to represent the number

  so, 2^15 = 32768

  - 0 | 0 to 32767 (positive numbers)
  - 1 | 0 to 32767 (negative numbers)
    since, there can't be -0, so considering upto -32768.

- Char data type range (1 byte)
  bits : 8 7 6 5 4 3 2 1 0

  we know, 2^7 = 128

  - 0 | 0 to 127 (positive numbers)
  - 1 | 0 to 127 (negative numbers)
    since, there can't be -0, so considering upto -128

> **Note:** Negative numbers are always stored in 2's complement
>
> for example, 12 = 0000000000001100
>
> -12 : 12's 1's complement = 1111111111110011 : add 1 to it = 1111111111110100
>
> -12 = 1111111111110100
>
> For viewing decimal of a binary negative number (e.g. 1111111111110100)
>
> we has to find 2's complement of this number and then convert it to decimal and then add -ve sign.

### Data type modifiers

- usigned (can only be used with int and char)

  `unsigned int` will have range 0 to 65535 , since It won't contain any negative numbers (only positive numbers)

  we know, 2^16 = 65536

  `unsigned chat` will have range 0 to 255, since it won't contain any negative numbers (only positive numbers)

  we know, 2^8 = 256

- long (cannot be used with char)

  `long int` will have size 4 bytes (Initially 2 bytes)

  `long float` will have size 8 bytes (Initially 4 bytes)

  `long double` will have size 10/16 bytes (Initially 8 bytes)

  > **Note:** : long float = double , so no need to use long float

### Initialization

These are different ways to initialize int

```cpp
    int day = 1;
    int day(1);
    int day = (1);
    int day {1};
    int day = {1};
```

### Literals

```cpp
    int a = 10;
    int a = 010; // Octal representation if 8
    int a = 0x41; // Hexadecimal representation of 65
```

> **Note:** : the calculations will happen in decimal system only , by default

```cpp
    long price = 65359L;
    float price = 12.5F;
```

```cpp
    char section = 'A';
    char section = 65;
```

#### Coersion

If a value is converted to required datatype internally, then it is called coersion.

```cpp
    char x = 65.6;          => A
```

```cpp
    float x = 123.45F;        => 123.45
```

```cpp
    float x = 123e2F;       => 12300
```

```cpp
    float x = 123e-2F;       => 1.23
```

### Operators and Expressions

If two integers are divided then, the result will also be of the integer type;

```cpp
    int a=13, b=5,c;
    c = a/b;                => 2
```

To get original result

```cpp
    int a=13, b=5;
    float c;                                    // c should hold the float value
    c = (float) a/b;             => 2.6         // Implicit type casting

```

```cpp
    int a=13;
    float c;
    c = a / 5.0;                => 2.6
```

> **Note:** : % operator can be performed on "int" and "char" , but not on "float"

#### Compound Assignment

```cpp
    sum = sum + a + b + c;
```

is same as the following

```cpp
    sum += a + b + c;
```

### Overflow

When the datatype value is increased by its limit, then it will overflow
and the result will be in cyclic order. (-128 | 0 | 127)

```cpp
    char b=127;
    b++;
    cout<<(int)b<<endl;         => -128 //since 128 value doesn't exist for char
```

```cpp
    char d=-128;
    d--;
    cout<<(int)d<<endl;         => 127 //since -129 value doesn't exist for char
```

### Left shift and right shift

```cpp
    char a=5, b, i=1;
    b = j<<i; // left shift by 1
    cout<<(int)b<<endl;            => 10 // value is a*(2^i)
```

```cpp
    char a=20, b, i=1;
    b = a>>1; // right shift by 1
    cout<<(int)m<<endl;             => 10 // value is a/(2^i)
```

> **Note:** : signed bits are not disturbed in the shift operation

### Enum and typedef (user defined data types)

```cpp
               0    1    2    3    4    5   6
    enum day {mon, tue, wed, thu, fri, sat, sun};
    day d = mon;    // d will get value 0;
```

```cpp
                      2    3    4     5   6    7
    enum day {mon=1, tue, wed, thu, fri, sat, sun};
```

```cpp
                      2           6    7          10
    enum day {mon=1, tue, wed=5, thu, fri, sa=9, sun};
```

```cpp
    typedef int marks;
    marks m1, m2, m3;
```

---

## Conditional Statements

### Dynamic Declaration

This method is not memory efficient because it is declared in the main function and will occupy the memory until the program terminates(main function gets over).

```cpp
    int c = a + b;
    if (c > 10) {
        // do something
    }
```

This approach is better , that declare a variable inside a simple block and then the do processing.

After the block is finished executing, the memory allocated to the variable will be deleted.

```cpp
    {
        int c = a + b;
        if (c > 10)
        {
            // do something
        }
    }
```

This feature was introduced in C++17 , and it works exactly same as previous approach.

```cpp
    if(int c = a + b; c > 10)
    {
        // do something
    }
```

Another way to use this feature

```cpp
    if(int e=a*b)
    {
        cout<<e<<endl;
    }
```

There is declaration and assignment in the if condition, which will return true and the block will get executed.

The memory allocated to the variable will be deleted after the block is finished executing.

### Switch case - Branch and control statement

Switch cases are faster than if else ladder.

We can write the default anywhere inside the switch block.

# Arrays

## for each loop

```cpp
    int A[5] = {2,4,6,8};
    for(int x : A)
        cout << x;              => 2 4 6 8 0
```

This will iterate over each element of the array.

We get copied value from the array (not the reference of the array elements.)

```cpp
    int A[5] = {2,4,6,8};
    for(int x : A)
        cout << ++x;              => 2 4 6 8 0
```

The value of array elements will not be changed.

```cpp
    int A[5] = {2,4,6,8};
    for(int &x : A)
        cout << ++x;              => 3 5 7 9 1
```

Now , the value of array elements will changed because of reference to the array elements.

```cpp
    int A[5] = {2,4,6,8};
    for(auto x : A)
        cout << x;              => 2 4 6 8 0
```

`auto` will determine the datatype of array and change datatype of x accordingly.

### for each loop for 2D arrays

```cpp
    int A[2][3] = {2,4,6,8,10,13};

    for(auto& x : A)
    {
        for(auto& y : x)
        {
            cout<<y<<" ";
        }
        cout<<endl;
    }
```

It is necessary to use & operator with `auto`, because x is a row of the array.

But for y we can use int as well, since it is a element of the array(row).

```cpp
    int A[2][3] = {2,4,6,8,10,13};

    for(auto& x : A)
    {
        for(int y : x)
        {
            cout<<y<<" ";
        }
        cout<<endl;
    }
```

# Pointers

## Pointer Arithematic

```cpp
    int A[5]={2,4,6,8,10};
    int *p = A;

    cout<<*p;               => 2

    p++;
    cout<<*p;               => 4

```

Performing incerement/decrement operation doesn't increases the address by one value, but the pointer goes to the next element.

```cpp
    int A[5] = {2,4,6,8,10};
    int *p = A;

    cout<<*p;               => 2

    p = p+2;
    cout<<*p;               => 6

        //OR

    cout<<*(p+2);           => 6
```

It points to the p + 2 element.

```cpp
    int A[5] = {2,4,6,8,10};
    int *p = &A[0], *q = &A[4];

    cout<< q - p;             => 4
    cout<< p - q;             => -4
```

> Summery : Arithematic operations does not operate on addresses , but on the pointers directly.

## Pointer to a function

```cpp
    void Display()
    {
        cout<<"Hello";
    }

    int main()
    {
        void (*fp)();           // Declaration
        fp = Display;           // Initialization
        (*fp)();                // Function Call
    }
```

```cpp
    int max(int a, int b)
    {
        return a > b ? a : b;
    }
    int min(int a, int b)
    {
        return a < b ? a : b;
    }

    int main()
    {
        int (*fp)(int, int);

        fp = max;
        (*fp)(10,5);            // Max function will be called

        fp = min;
        (*fp)(10,5);            // Min function will be called
    }
```

## References

Reference is a Alias of variable

- It must be initialised during the declaration
- It doesn’t take any memory
- It cannot be modified to refer other variable
- Syntax for reference declaration is
- `int &y = x;`

# Functions

- Functions can return a single value
- Default return type is `int`

## Function Overloading

- If More than one functions can have same name, but different parameter list, then they are overloaded functions
- Return the is not considered in overloading
- Function overloading is used for achieving compile time polymorphism

## Function Template

- Function template are used for defining "generic functions"
- They work for multiple datatypes
- Datatype is decided based on the type of value passed
- Datatype is a template variable
- Function can have multiple template variables

```cpp
    template <class T>
    T maxi(T x, T y)
    {
        return (x > y) ? x : y;
    }

    template <class T, class U>
    U add(T x, U y)     // we have set return "type" to "type" of second parameter
    {
        return (x + y);
    }

    int main()
    {
        cout << maxi(5, 10) << endl;            => 10
        cout << add(5, 10.2) << endl;           => 15.2
        return 0;
    }
```

## Returning from a function

### Return by Address

- A function can return address of memory
- It should not return address of local variables, which will be disposed after function ends
- It can return address of memory allocated in heap

```cpp
    int * fun(int n)
    {
        int *p = new int[n];
        for(int i=0; i<n; i++)
            p[i] = i + 1;
        return p;
    }

    int main()
    {
        int *ptr = fun(5);
        for(int i=0; i<5; i++)
            cout<<i<<endl;
        return 0;
    }
```

### Return by Reference

- It should not return reference of its local variables
- It is written on left side of the assignment operator

```cpp
    int& min(int &a, int &b)
    {
        if(a < b)
            return a;
        else
            return b;
    }

    int main()
    {
        int a=10, b=20;
        min(a,b) = 0;
        cout<<a;                    => 0
        cout<<b;                    => 20
    }
```

## Static Variables

- They have local scope but remain in memory through out the execution of program
- They are created in code section
- They are history-sensitive

```cpp
    void fun()
    {
        static int v=0;
        int a=10;
        v++:
        cout<<a<<“ “<<v;
    }
    int main()
    {
        fun();              => 10 1
        fun();              => 10 2
        fun();              => 10 3
    }
```
