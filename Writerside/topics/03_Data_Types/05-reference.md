# Reference
<show-structure depth="2"/>

A reference is an alias for an existing variable.

It does not create a new object. It doesn’t take any memory

It is just another name for the same memory.

```c++
int x = 10;
int& ref = x;
```

**1. Reference must be initialized**
```c++
int& r;         // error
// Reference cannot be NULL
// Unlike pointers, references must refer to something valid... 
// This alone makes them safer than pointers.

int x = 10;
int& r = x;     // valid
```

**2. Reference must match the type**
```c++
int x = 10;
double& r = x;   // error
```

**3. Reference cannot be changed to refer to another variable**
```c++
int x = 10, y = 20;
int& r = x;

r = y;    // assigns y's value to x, does NOT rebind reference
```

After this:
```c++
x = 20
y = 20
```

`r` still refers to `x`.