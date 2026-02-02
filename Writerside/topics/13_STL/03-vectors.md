# Vectors

```c++
std::vector<T>
```

A dynamic array that:
- Stores elements in contiguous memory
- Grows automatically
- Supports random access
- Knows its own size

```c++
vector<int> v = {1, 2, 3};
```

## Memory layout

Internally:
```
| 1 | 2 | 3 | 4 | _ | _ | _ |
```

- Contiguous block
- Extra unused space = capacity
- When capacity runs out → allocate bigger block → copy → delete old

## Size vs Capacity

```c++
v.size();     // number of elements
v.capacity(); // allocated space
```

```c++
vector<int> v;
v.push_back(1);
v.push_back(2);
```

Possible state:
```c++
size = 2
capacity = 4
```

Capacity grows exponentially. Usually 2x.

## Creating vectors

```c++
vector<int> v1;              // empty
vector<int> v2(5);           // 5 zeros
vector<int> v3(5, 10);       // 5 tens
vector<int> v4 = {1, 2, 3};  // initializer list
```

Copy:
```c++
vector<int> v5 = v4;
```

## Accessing elements

```c++
v[i]; // no bounds check
v.at(i); // throws exception if out of range
v.front();
v.back();
```

## Adding elements

```c++
v.push_back(10);
```

## Removing elements

```c++
v.pop_back();        // removes last
v.clear();           // removes all

// Remove by index
v.erase(v.begin() + i);
```

O(n)

## Insert elements

```c++
v.insert(v.begin() + 2, 100);
```

Insert 100 at 2nd index.

O(n)

## Iterators

```c++
for (auto it = v.begin(); it != v.end(); it++) {
    cout << *it;
}

for (int x : v) cout << x;

// Reverse iterators
for (auto it = v.rbegin(); it != v.rend(); it++) {}
```

## Sorting and algorithms

```c++
sort(v.begin(), v.end());
reverse(v.begin(), v.end());
binary_search(v.begin(), v.end(), 5);
```

## Reserving memory (performance trick)

```c++
v.reserve(1000);
```

Pre-allocates capacity.

Prevents repeated reallocations.

Use this when size is known ahead.

## Shrinking memory

```c++
v.shrink_to_fit();
```

## Passing vectors to function

When we **pass the vector by value**, the complete vector gets copied, and then passed. Unlike arrays.

So, usually vectors are **passed by reference** to avoid copying.

## Time Complexity Summary

| Operation                | Complexity     |
|--------------------------|----------------|
| Access                   | O(1)           |
| push_back                | O(1) amortized |
| insert/erase (middle)    | O(n)           |
| search (unsorted)        | O(n)           |
| search (sorted + binary) | O(log n)       |
