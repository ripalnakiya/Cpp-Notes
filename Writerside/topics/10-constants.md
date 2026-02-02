# Constants

syntax:

```c++
const int a = 10;

int const a = 10;
```

## Constant Formal Parameters

When we use **call by reference**, the actual variables are used in the function. 

Those variables can also be altered in the function.

To avoid this problem,
we can declare the formal parameters as `const`,
so that the parameters will stay constant
during the execution of function and its value will not be changed.

```c++
void fun(const int& x, const int& y)
{
    x++; // ❌ This statement will give error
    cout << x << " " << y << endl;
}

int main()
{
    int a = 10, b = 20;
    fun(a, b);
}
```

## Constant Methods

If a member function of a class is not allowed to change the data members of class, 
then we can use `const` keyword after the function name.

```c++
class Marks
{
public:
    int x = 10;
    int y = 20;

    void Display() const
    {
        x++; // ❌ This statement will give error
        cout<< x << " " << y << endl;
    }
}
```

## Constants and Pointer

### Pointer to const

```c++
int a = 10, b = 20;

const int* ptr = &a;
```

- The pointer itself is **not const** → it can point to another address
- The value pointed to is treated as **read-only through this pointer**

```c++
*ptr = 15;   // ❌ Invalid: cannot modify the value through ptr
ptr = &b;    // ✅ Valid: ptr can point somewhere else
```

`a` itself is not const.
You just promised the compiler you won’t modify it _via this pointer_.

### Pointer to const variable

This is the same type as above.

The _pointed object_ happens to be const.

```c++
const int a = 10, b = 20;

const int* ptr = &a;   // ✅ Correct

// You cannot assign a `const int*` to an `int*`
// That would allow modifying a const object

int* p = &a; // ❌ Invalid
```

```c++
ptr = &b;    // ✅ Valid
*ptr = 25;   // ❌ Invalid: pointed value is const
```

### Const pointer to a variable

The pointer is const, not the data.

```c++
int a = 10, b = 20;

int* const ptr = &a;
```

- The pointer always points to the same address
- The value at that address can be modified

```c++
ptr = &b;   // ❌ Invalid: ptr itself is const
*ptr = 15;  // ✅ Valid
```

### Const pointer to const data

We can neither change the address to which the pointer is pointing at,
nor change the value at that address.

```c++
const int a = 10, b = 20;

const int* const ptr = &a;
```

```c++
ptr = &b;   // ❌ Invalid
*ptr = 15;  // ❌ Invalid
```
