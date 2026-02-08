# Pointer
<show-structure depth="2"/>

Pointer is a variable that holds a memory address of a resource.

```c++
int a = 15;
int *p;
p = &a;

cout << p;          // 0xC3h8
cout << *p;         // 15
```

Data type of pointer decides which resource the pointer can point to.

## Pointer Arithmetic

Only integers can be added and subtracted from pointers.

No other arithmetic operations are allowed on pointers.

```c++
    int A[5]={2,4,6,8,10};
    int *p = A;

    cout<< *p;               => 2

    p++;
    cout<< *p;               => 4
```

Performing incerement/decrement operation doesn't increase the address by one value, 
but the pointer goes to the next element.

```c++
    int A[5] = {2,4,6,8,10};
    int *p = A;

    cout<<*p;                   => 2

    p = p + 2;
    cout<< *p;                  => 6

    cout<< *(p + 2);            => 10
```

> Summery : Pointer arithmetic is type-aware and advances by sizeof(type), not by raw bytes.
{style="note"}

### Two Pointers

Arithmetic operations between two pointers are not allowed, 
except subtraction (when both point into the same array).
```c++
    int A[5] = {2,4,6,8,10};
    int *p = &A[0], *q = &A[4];

    cout << q - p;   => 4   // (Difference b/w p and q pointer is of 4 int)
    cout << p - q;   => -4

    cout << p + q;   => -4  // Error
```

- Pointer ± integer → ✅
- Pointer − pointer → ✅ (same array only)
- Pointer + pointer → ❌

## new and delete

Pointers can avail memory from heap during the program run.

`new` operator allocates the memory dynamically and 
returns a pointer storing the memory address of the allocated memory.

```c++
// Method 1
int *iPtr;
iPtr = new int;
*iPtr = 10;

// Method 2
int *iPtr = new int;
*iPtr = 10;

// Method 3
int *iPtr = new int(10);
```

All 3 methods achieve the same thing.

We can create arrays dynamically:
```c++
int *iArr = new int[10];

int *iArr = new int[]{17, 3, 7, 9, 2};
```

**`new` returns `NULL` when enough requested memory is not available.**

The lifetime of the object created by `new` is not restricted to the scope in which it is created.
It lives in the memory until explicitly deleted using the `delete` operator.

```c++
delete iPtr;
delete[] iArr;
```

> **Memory Leak:** Improper use of new and delete may lead to memory leaks.
{style="warning"}

> **Orphaned memory block:** A block that is still allocated, but nothing can access it.
{style="warning"}

## Pointers and Arrays

Name of the array is a pointer, that points to the first index.

```c++
int arr[10] = {2, 7, 9, 14, 17}; 

cout << *arr;       // 2
cout << *(arr+3)    // 14
cout << *(arr++)    // Error: We cannot modify the array pointer
```

## Array of Pointers

```c++
int *ip[10];
// ip is and array of 10 elements
// each element is a pointer to int
```

Memory will be allocated for 10 pointers that can point to integer variables.

```c++
int a = 17;
int b = 23;
*(ip) = &a;
*(ip + 3) = &b;

cout << *(ip + 3);  // 0x23gD - Address of varialbe b
cout << *(*(ip + 3)); // 23 - Value stored in variable b

cout << *(ip);      // 0xE86r - Address of variable a
cout << *(*(ip));     // 17 - Value stored in variable a
```

Define array of pointers dynamically:
```c++
int *(*ip) = new int* [10];

int b = 23;
*(ip + 3) = &b;

cout << *(*(ip+3));     // 23
```

## Pointer and String

```c++
char *name = "FooBar";
// char name[6] = "FooBar";
// char name[6] = {'F', 'o', 'o', 'B', 'a', 'r'};
char *cp = name;

cout << cp;     // FooBar
cout << cp[0];   // F
cout << *(cp);  // F

cp += 2;
cout << cp;     // ooBar
cout << cp[0];  // o
cout << *(cp);  // o
```

### Array of Strings

```c++
char *name[10] = {"Foo", "The", "Bar"};
// name is an array of 10 elements
// each element is a pointer to (char *)
//
// the pointers are initialized to point to string literals
// each pointer points to the first character of its string,
// So the full string is accessed via that address

cout << name[0];        // Foo
cout << *(name);        // Foo
cout << **(name);       // F
cout << **(name + 1);   // o
```
