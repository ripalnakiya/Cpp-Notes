# Functions
<show-structure depth="2"/>

- The parameters that appear in 
  - a function call statement are **actual** parameters.
  - function definition are **formal** parameters.

## Parameter Passing Techniques

**1. Pass by value**
```c++
void print(int x, int y);

print(5, 10);
```

**2. Pass by Address**
```c++
void print(int *x, int *y);

int a = 5;
int b = 10;
print(&a, &b);
```

**3. Pass by Reference**
```c++
void print(int &x, int &y);

int a = 5;
int b = 10;
print(a, b);

print(5, 10);    // Error
```

## Returning from function

Functions can return only a single value.

**1. Return by value**
```c++
int min(int a, int b)
{
    if (a < b)  return a;
    return b;
}

int a = 10, b = 20, c;
c = min(a,b);
```

**2. Return by address**

```c++
int* min(int &a, int &b)
{
    if (a < b)  return &a;
    return &b;
}

int a = 10, b = 20, *c;
c = min(a,b);
```

- A function can return address of memory.
- It can return address of memory allocated in heap. 
- It should not return address of local variables, which will be disposed after function ends.

**3. Return by reference**
```c++
int& min(int &a, int &b)
{
    if (a < b)  return a;
    return b;
}

int a = 100;
int b = 90;
min(a, b) = -1;
```

- Function is written on left side of the expression.
- It should not return reference of its local variables

## Default Parameters

Any argument cannot have a default value 
unless all arguments appearing on it's right have default values.

```c++
float interest(float p, int t = 2, float r = 10.0); // Valid
float interest(float p, int t = 2, float r);        // Error
```

## Arrays

**Passing array to function**

Arrays are always **passed by reference** in functions.

```c++
void display(int a[10]);

display(arr);
```

```c++
void display(int a[]);

display(arr);
```

```c++
void display(int *a);

display(arr);
```

**Returning array from function**

```c++
int [] function(int n);
int* function(int n);
```

## Pointer to a function

```c++
void Display(int a)
{
    cout << a;
}

int main()
{
    void (*fp)(int);            // Declaration
    fp = Display;               // Initialization
    
    // fp is a pointer that points to function having 
    // return type void and (int) as signature
    
    int a = 10;
    (*fp)(a);                   // Function Call
    fp(a);                      // Function Call
}
```

```c++
// Function that is returning a integer pointer
int *fp(int, int);  

// Pointer fp to a fuction having return type int and signature (int, int)
int (*fp)(int, int);
```


```c++
int max(int a, int b)
{   return a > b ? a : b;   }
int min(int a, int b)
{   return a < b ? a : b;   }

int main()
{
    int (*fp)(int, int);

    fp = max;
    (*fp)(10,5);            // Max function will be called
    
    fp = min;
    (*fp)(10,5);            // Min function will be called
}
```


### Passing function pointers to functions

```c++
int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

int operate(int a, int b, int (*op)(int, int)) {
    return op(a, b);
}

operate(3, 4, add); // 7
operate(3, 4, mul); // 12
```

### Array of function pointers

```c++
int add(int, int);
int sub(int, int);
int mul(int, int);

int (*ops[])(int, int) = { add, sub, mul };

ops[0](5, 2); // add
ops[1](5, 2); // sub
ops[2](5, 2); // mul
```

State machines, menu systems, interpreters use this.

### Simplify with typedef

```c++
int add(int a, int b) {
    return a + b;
}

// Create function pointer type using typedef
typedef int (*Operation)(int, int);

// Function that takes a function pointer
int operate(int x, int y, Operation op) {
    return op(x, y);
}

int main() {
    Operation op = add;
    cout << operate(10, 20, op) << endl;
    return 0;
}
```

### Simplify with using

```c++
int add(int a, int b) {
    return a + b;
}

// Create function pointer type using using
using Operation = int (*)(int, int);

// Function that takes a function pointer
int operate(int x, int y, Operation op) {
    return op(x, y);
}

int main() {
    Operation op = add;
    cout << operate(10, 20, op) << endl;
    return 0;
}
```
