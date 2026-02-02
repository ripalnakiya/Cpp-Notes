# Type safe

The language prevents you from using a value as the wrong type
and catches such mistakes at compile time (or runtime)
instead of letting your program quietly misbehave.

```c++
int x = 10;
double* p = (double*)&x;   // allowed in C++
```

This compiles successfully.
It should not.
This is **not type-safe** behavior.

## Example 1

```c++
enum Color { RED, GREEN };
int x = RED;   // allowed since RED is a int after all (classic enum)
```

Here:
- `RED` becomes an `int`
- Compiler doesn’t stop you
- Less type-safe

```c++
enum class Color { RED, GREEN };
int x = Color::RED;   // ❌ error
```

Here:
- Compiler enforces the type
- You must be explicit
- This is type-safe.

## Example 2

```c++
void print(int x);

print(3.14);   // allowed (coercion)
```

C++ converts `double` → `int` silently.
That’s less type-safe.

More type-safe approach:
```c++
void print(double x);
```
