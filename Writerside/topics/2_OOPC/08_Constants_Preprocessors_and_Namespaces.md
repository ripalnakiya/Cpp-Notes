# Constants Preprocessors and Namespaces

## Constants

syntax:

`const int a = 10;`

or

`int const a = 10;`

### Constant Identifiers

We cannot point to a constant identifier , using variable pointer.

```cpp
    const int x = 10;
    int *ptr = &x;          // Invalid Statement
```

But this is possible,

```cpp
    const int x = 10;
    const int *ptr = &x;          // Valid Statement
```

### Pointer to Constant (Data is Constant)

In the pointers to constant, the data pointed by the pointer is constant and cannot be changed. Although, the pointer itself can change and points somewhere else (as the pointer itself is a variable).

#### Base Operation

```cpp
    int x = 10;
    int *ptr = &x;
    ++(*ptr);       // Valid statement
```

#### Operation on constant type pointer

```cpp
    int x = 10;
    const int *ptr = &x;
    ++(*ptr);       // Invalid statement (we cannot modify the data value of the pointer to constant)
```

Here, `ptr` is a pointer to integer constant, so the ptr will treat x as a constant.

Pointer assumes that it is pointing to a constant type variable.

It can also be written as `int const *ptr = &x;`

#### Assigning another constant to the pointer

```cpp
    int x = 10;
    const int *ptr = &x;
    ++(*ptr);       // Invalid statement

    int y = 20;
    ptr = &y;       // Valid statement
    ++(*ptr);       // Invalid statement
```

Here, the pointer is NOT constant (It is a variable) , but the value pointed by pointer is constant.

### Constant Pointer (Pointer is constant)

In constant pointers, the pointer points to a fixed memory location, and the value at that location can be changed because it is a variable, but the pointer will always point to the same location because it is made constant here.

```cpp
    int x = 10;
    int * (const ptr) = &x;
    ++(*ptr);       // Valid statement

    int y = 20;
    ptr = &y;       // Invalid statement
```

### Constant Pointer to Constant

The data pointed to by the pointer is constant, so cannot be changed and The pointer itself is constant, so it cannot change or point somewhere else.

```cpp
    int x = 10;
    const int * const ptr = &x;
    ++(*ptr);       // Invalid statement

    int y = 20;
    ptr = &y;       // Invalid statement
    ++(*ptr);       // Invalid statement
```

### Constant Methods

If a Member function of a class is not allowed to change the data members of class, then we can use `const` keyword after the fucntion name.

```cpp
class Demo
{
    public:
        int x = 10;
        int y = 20;

        void Display() const
        {
            x++;                // Now, this statement will give error
            cout<< x << " " << y << endl;
        }
}
```

### Constant Formal Parameters

```cpp
void fun(const int &x, const int &y)
{
    x++;                            // This statement will give error
    cout<< x << " " << y << endl;
}

void main()
{
    int a = 10, b = 20;
    fun(a,b);
}
```

When we use call by reference, the actual variables are used in the function.

Those variables can also be altered in the fucntion.

To avoid this problem, we can declare the formal parameters as `const`, so that the parameters will stay constant during the execution of function and its value will not be changed.

## Preprocessor Directives (Macros)

They are instructions to compiler.

They are processed before compilation.

The replacement is performed before the compilatioon.

They are used for defining symbolic constant.

They are used for defining functions.

They also support conditional definition.

---

```cpp
#define PI 3.14

void main()
{
    cout<<PI;           => 3.14
}
```

---

```cpp
#define PI 3.14
#define PI 3

void main()
{
    cout<<PI;           => 3
}
```

---

`ifndef` is conditional directive, which means "If not defined"

```cpp
#define PI 3.14

#ifndef PI
    #define PI 3
#endif

void main()
{
    cout<<PI;           => 3.14
}
```

Here , if value of PI is not defined already, then It will get executed.
But since we already have defined PI, so It won't get executed.

---

```cpp
#ifndef PI
    #define PI 3
#endif

void main()
{
    cout<<PI;           => 3
}
```

Since we haven't already defined the value of PI, so it will get executed.

---

```cpp
#define maxi(a,b) (a > b ? a : b)

void main()
{
    cout<< maxi(10,12);         => 12
}
```

---

```cpp
#define msg(x) #x

void main()
{
    cout<< msg(Hello);          => Hello
}
```

`#` before `x` makes the value of `x` as string (It wraps the value of x in double quotes).

Here, it changes it into `"Hello"`

## Namespaces

They are used for removing name conflict between functions, classes and objects.

### Base Problem

```cpp
void fun()
{
    cout<< "First" <<endl;
}

void fun()
{
    cout<< "Second" <<endl;
}

void main()
{
    fun();
}
```

This program will give error that , redeclaration of funtion `fun()` is done.

### Using Namespaces

```cpp
namespace first
{
    void fun()
    {
        cout<< "First" <<endl;
    }
};

namespace second
{
    void fun()
    {
        cout<< "Second" <<endl;
    }
};

void main()
{
    fun();              // Statement 1 : Invalid Statement
    first::fun();       => First
    second::fun();      => Second
}
```

`statement 1` will give error because function `fun()` is not openly declared.

---

```cpp
namespace first
{
    void fun()
    {
        cout<< "First" <<endl;
    }
};

namespace second
{
    void fun()
    {
        cout<< "Second" <<endl;
    }
};

using namespace first;
void main()
{
    fun();              => First        // Valid Statement
    second::fun();      => Second
}
```