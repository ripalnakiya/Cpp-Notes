# Variables

## Declaring Variables with Limited Scope

**1. Variable declared in a wider scope**

```c++
int c = a + b;
if (c > 10) {
    // do something
}
```

Here, `c` is declared in the surrounding scope (for example, inside `main`),
so it remains alive until that scope ends.

This is not memory efficient in terms of scope, because `c` exists longer than needed.

**2. Variable declared inside a block**

```c++
{
    int c = a + b;
    if (c > 10) {
        // do something
    }
}
```

In this approach, `c` is limited to this block.

Once the block finishes executing:
- `c` goes out of scope
- its memory is released automatically

This is better because the variable exists only where it is needed.

**3. Variable declared inside `if` (C++17)**

```c++
if (int c = a + b; c > 10) {
    // do something
}
```

This syntax was introduced in C++17.
- `c` is created only for this `if` statement
- It behaves exactly like the previous block-based approach
- `c` is destroyed after the `if` statement finishes

This is the cleanest and safest way when a variable is only needed for a condition.

**4. Using declaration directly as a condition**

```c++
if (int e = a * b) {
    cout << e << endl;
}
```

Here:
- `e` is declared and initialized inside the if
- The condition is true if `e` is non-zero
- `e` is destroyed after the if block

Again, the variable lives only as long as necessary.

> If there is declaration or assignment in the `if` condition, then it will return true and the block will get executed.

If the expression in the `if` condition evaluates to `0`,
then `if` condition will not be executed, because expression has evaluated to `false`.

```c++
if (int a = b * 0)
    cout << a;      // Will not be printed

if (int a = 0)
    cout << a;      // Will not be printed
```
