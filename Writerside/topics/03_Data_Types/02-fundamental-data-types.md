# Fundamental data types
<show-structure depth="2"/>

**Integer Types**

| Data Type       | Minimum Size (Standard) | Common Size (64-bit systems)             |
|-----------------|-------------------------|------------------------------------------|
| `bool`          | 1 byte                  | 1 byte                                   |
| `char`          | 1 byte                  | 1 byte                                   |
| `signed char`   | 1 byte                  | 1 byte                                   |
| `unsigned char` | 1 byte                  | 1 byte                                   |
| `short`         | ≥ 2 bytes               | 2 bytes                                  |
| `int`           | ≥ 2 bytes               | 4 bytes                                  |
| `long`          | ≥ 4 bytes               | 8 bytes (Linux/macOS), 4 bytes (Windows) |
| `long long`     | ≥ 8 bytes               | 8 bytes                                  |

**Floating-Point Types**

| Data Type     | Minimum Size | Common Size                               |
|---------------|--------------|-------------------------------------------|
| `float`       | ≥ 4 bytes    | 4 bytes                                   |
| `double`      | ≥ 8 bytes    | 8 bytes                                   |
| `long double` | ≥ 8 bytes    | 16 bytes (Linux), 8 or 16 bytes elsewhere |

**Pointer Types**

| Type                                | Size                    |
|-------------------------------------|-------------------------|
| Any pointer (`int*`, `char*`, etc.) | 4 bytes (32-bit system) |
|                                     | 8 bytes (64-bit system) |

All pointers have the same size on a given system. The type they point to is irrelevant.

## Representation range

Assumption: `int` is 2 bytes (16 bits) and uses two’s complement representation.

```python
Bits: 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
```

The MSB (Most Significant Bit) represents the sign
- `0` → positive
- `1` → negative

Remaining 15 bits are used to represent the value

Total values: `2^16 = 65536`

Range:
- Positive: 0 to +32767
- Negative: -32768 to -1

Reason for asymmetry:
- There is no −0 in two’s complement
- One extra value goes to the negative side

> Negative integers are typically stored using two’s complement representation.
> Example: `-12` (16-bit)
> 1. Binary of `+12`: `0000000000001100`
> 2. 1’s complement (invert bits): `1111111111110011`
> 3. Add 1 → 2’s complement: `1111111111110100`
> 4. `-12` = `1111111111110100`

## Initialization

These are different ways to initialize `int`

```c++
    int day = 1;
    int day(1);
    int day = (1);
    int day {1};
    int day = {1};
```

### Literals

```c++
    int a = 10;
    int a = 010;    // Octal representation if 8
    int a = 0x41;   // Hexadecimal representation of 65
```

> **Note:** : the calculations will happen in decimal system only , by default
{style="note"}

```c++
    long price = 65359L;
    float price = 12.5F;
```

```c++
    char section = 'A';
    char section = 65;
```

## Data type conversion

### Coercion (Implicit)

Coercion is the automatic conversion of one data type into another by the compiler.

1. Coercion in assignment
```c++
char x = 65.6;              => A
char c = 100;               // int → char

int a = 10;
double b = a;               // int → double (coercion)

float x = 123.45F;          => 123.45
float x = 123e2F;           => 12300
float x = 123e-2F;          => 1.23
```

2. Coercion in arithematic operations
```c++
int x = 5;
double y = 2;
double z = x / y;           => 2.5  // x is coerced from int to double                            

int a = 10;
float b = 3.5;
auto c = a + b;             // int → float
// Smaller types get promoted to larger ones.
```

3. Coercion in function arguments
```c++
void print(double x);

print(10);  // int → double
```

### Type Casting (Explicit)

Forced by the programmer.

```c++
int x = (int)3.7;        // C-style cast
int y = static_cast<int>(3.7);  // C++-style cast
```

### Coercion can be dangerous

```c++
int a = 5;
int b = 2;
double c = a / b;  // result = 2, not 2.5
```

- Why?
  - `a / b` is integer division
  - Result becomes `2`
  - Then it’s coerced to `2.0`

Too late. Damage done.

Correct way:
```c++
double c = static_cast<double>(a) / b;
```
