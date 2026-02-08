# Pairs
<show-structure depth="2"/>

```c++
std::pair<T1, T2>
```

- It stores:
  - `first` → type `T1`
  - `second` → type `T2`

```c++
pair<int, string> p = {1, "apple"};
```

## When to use ?

- Return two values from a function
- Store key–value-like data without a full struct
- Use it inside `map`, `set`, `priority_queue`, etc.

## Initialisation

```c++
pair<int, int> p(10, 20);

pair<int, int> p = {10, 20};

auto p = make_pair(10, "hello");
```

## Accessing values

```c++
cout << p.first << " " << p.second;
```

## Pair comparison

Pairs are compared lexicographically.

- Order:
  - Compare `first`
  - If equal, compare `second`

```c++
pair<int, int> a = {1, 5};
pair<int, int> b = {2, 1};

a < b   // true
```
## pair vs tuple

`pair` → exactly 2 values

`tuple` → 2 or more values

```c++
tuple<int, int, int> t;
```
