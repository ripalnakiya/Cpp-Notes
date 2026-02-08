# Operators and Expressions
<show-structure depth="2"/>

`%` operator can only be performed on integer types (`int` and `char`), but not on `float`.

## Overflow

When the datatype value is increased by its limit, then it will overflow
and the result will be in cyclic order. `(-128 | 0 | 127)`

```c++
    char b = 127;
    b++;
    cout << (int)b << endl;         => -128 //since 128 value doesn't exist for char
```

```c++
    char d =- 128;
    d--;
    cout << (int)d << endl;         => 127 //since -129 value doesn't exist for char
```

## Left and Right Shift

```c++
    char a = 5, b, i = 1;
    b = j << i; // left shift by 1
    cout << (int)b << endl;            => 10 // value is a*(2^i)
```

```c++
    char a = 20, b, i = 1;
    b = a >> 1; // right shift by 1
    cout << (int)m << endl;             => 10 // value is a/(2^i)
```

> **Note:** : signed bits are not disturbed in the shift operation
{style="warning"}
