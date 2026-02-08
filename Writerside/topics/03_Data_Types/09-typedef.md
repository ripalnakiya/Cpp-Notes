# typedef
<show-structure depth="2"/>

`typedef` is used to create a type alias for an existing data type.

- No new data type is created
- Only an alternate name is given

```c++
typedef existing_type new_name;

typedef int marks;
marks m1, m2, m3;

typedef int Integer;
Integer x = 10;   // same as int
```

## typedef common usage

1. Simplifying Complex Types
```c++
typedef unsigned long long ull;
ull x = 100; 
```

2. `typedef` with Pointers (Important)
```c++
typedef int* IntPtr;
IntPtr p1, p2;   // both are pointers

int* p1, p2;     // p2 is NOT a pointer
```

3. `typedef` with Arrays
```c++
typedef int Arr[10];
Arr a;   // int a[10]
```

4. `typedef` with Structs
```c++
// C-style:
struct Student {
    int id;
};
typedef struct Student Student;

// Modern C++:
struct Student {
    int id;
};
// No typedef needed
```

5. `typedef` with function pointers
```c++
typedef int (*Operation)(int, int);

Operation add;              // `add` is name of the function
```

**Type checking is not stricter**
```c++
MyInt a = 10;
int b = a;   // allowed
```

**`typedef` works at compile time:**

It’s resolved by the compiler. No runtime cost.

## using

- `using` creates a type alias.
- Makes complex types and templates much more readable.

```c++
using NewName = ExistingType;

using Integer = int;
Integer x = 10;  // same as int x = 10;
```

## using common usage

1. `using` with Pointers
```c++
using IntPtr = int*;

IntPtr a, b;   // both are int*
```

2. `using` with Arrays

```c++
using IntArray = int[10];

IntArray arr;  // int arr[10]
```

3. `using` with function pointers
```c++
using Operation = int(*)(int, int);

Operation add;              // `add` is name of the function
```

4. `using` with Templates (most important)
```c++
template<typename T>
using Vec = std::vector<T>;

Vec<int> v;   // std::vector<int>
```

- `typedef` can’t directly create template aliases
- `using` can, which is why it’s preferred in modern C++

**Type checking is not stricter**
```c++
using MyInt = int;

MyInt a = 10;
int b = a;   // allowed
```

**`using` works at compile time**

The alias is resolved by the compiler.
No extra runtime overhead.
