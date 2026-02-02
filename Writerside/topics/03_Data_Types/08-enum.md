# Enums

An enum (enumeration) is a user-defined data type that represents a set of named integral constants.

Instead of:
```c++
int status = 2;   // what is 2?
```

We write:
```c++
Status status = SUCCESS;  // readable
```

## Basic Syntax (Classic enum)

```c++
enum EnumName {
    CONSTANT1,
    CONSTANT2,
    CONSTANT3
};

// Example:
enum Color {
    RED,        // By default: RED = 0
    GREEN,      // By default: GREEN = 1
    BLUE        // By default: BLUE = 2
};
```

Using an enum:
```c++
Color c = RED;

if (c == GREEN) {
    // do something
}
```

Assigning Custom Values:
```c++
enum ErrorCode {
    OK = 0,
    NOT_FOUND = 404,
    SERVER_ERROR = 500
};
```

**1. Values must be integral constants**

**2. Unassigned values continue incrementing**

```c++
enum day {mon, tue, wed, thu, fri, sat, sun};
           0    1    2    3    4    5    6

enum day {mon = 1, tue, wed, thu, fri, sat, sun};
                    2    3    4    5    6    7

enum day {mon = 1, tue, wed = 5, thu, fri, sa = 9, sun};
                    2             6    7           10
```

**3. Enum names go into the same scope (classic enum)**

```c++
enum Color { RED, GREEN };
enum Traffic { GREEN, YELLOW }; // ❌ conflict
```

Classic enums pollute the namespace. This is why modern C++ fixed it.

## Scoped Enums

```c++
enum class Color {
    RED,
    GREEN,
    BLUE
};

// Usage:
Color c = Color::RED;
```

Why `enum class` is better:

| enum                    | enum class             |
|-------------------------|------------------------|
| Implicit int conversion | No implicit conversion |
| Pollutes scope          | Scoped                 |
| Less type-safe          | Strongly typed         |
