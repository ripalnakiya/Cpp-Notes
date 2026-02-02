# Flow of Control

In a program, the statements may get executed
- Sequentially
- Selectively (Decision construct)
- Iteratively (Looping construct)

## Selection Statements

### Dangling else

In nested `if`, the dangling `else` statement matches with the preceding unmatched `if` statement.

```c++
if (condition 1)
    if (condition 2)
        // Something
else
    // Something
```

This will be interpreted as the following, by compiler
```c++
if (condition 1)
    if (condition 2)
        // Something
    else
        // Something
```

### Switch case

- We cannot use floating point comparisons.
- Switch cases are faster than if else ladder.
- We can write the default anywhere inside the switch block.

## Iteration Statements

1. `for` loop
2. `while` loop
3. `do while` loop

## Jump Statements

**1. `break`**

Immediately exits the closest enclosing loop or `switch`.

**2. `continue`**

- Skips the remaining code in the current iteration
- Jumps to the next iteration
- Works only in loops

**3. `goto`**

- Works inside the same function
- It Uses labels

```c++
label:
    // code

goto label;
```

**4. `return`**

- Exits the function immediately
- Optionally returns a value
