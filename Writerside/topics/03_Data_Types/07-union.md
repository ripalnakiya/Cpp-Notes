# Union
<show-structure depth="2"/>

A union lets us store different data types in the same memory location. 

All members overlap. 

The size of the union is the size of its largest member, not the sum.

```c++
union Data {
    int i;
    float f;
    char c;
};
```

```c++
Data d;
d.i = 42;        // now the memory holds an int
d.f = 3.14f;    // overwrites the same memory as a float
```

## Memory behavior

```c++
sizeof(Data) == max(sizeof(int), sizeof(float), sizeof(char));
```

- All members:
  - Start at the same address
  - Share the same bytes
  - Are mutually exclusive in practice

## Important Info

- Only one member is active at a time
- Reading an inactive member → undefined behavior

## When to use union

1. **Memory-critical code**
Embedded systems, kernels, game engines.

2. **Interpreting raw data**
Hardware registers, network packets, binary file formats.


