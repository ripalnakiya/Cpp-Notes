# Sets
<show-structure depth="2"/>

## Set

```c++
std::set<T>

set<int> s = {5, 1, 3};
```

Internally becomes:
```
1 3 5
```

- Stores unique elements
- Automatically sorted
- Implemented using a balanced BST (Red-Black Tree)
- Order is determined by < (or a custom comparator)
- Elements are **immutable** (you can’t modify them directly)

**Why immutable?**
Because changing a value might break the tree ordering.

### Operations on set

```c++
s.insert(10);     // O(log n)
s.erase(3);       // O(log n)
s.find(5);        // O(log n)
s.count(5);       // 0 or 1
```

### Lower and upper bound on set

```c++
s.lower_bound(5); // pointer to first element that is >= 5
s.upper_bound(5); // pointer to first element that is > 5
```

## Multiset

```c++
std::multiset<T>

multiset<int> ms = {1, 2, 2, 3};
```

Stored as:
```
1 2 2 3
```

- Same as set
- Allows duplicates
- Still sorted
- Still tree-based

### Set vs Multiset

| Feature    | set         | multiset    |
|------------|-------------|-------------|
| Duplicates | ❌           | ✅           |
| Sorted     | ✅           | ✅           |
| count(x)   | 0 or 1      | 0 to n      |
| erase(x)   | removes one | removes all |

Erase one occurrence:
```c++
auto it = ms.find(2);
ms.erase(it);
```

## Unordered Set

```c++
std::unordered_set<T>

unordered_set<int> us = {5, 1, 3};
```

Stored like:
```
?? ?? ??    // Undefined.
```

- Stores unique elements
- No ordering
- Implemented using a hash table
- Average O(1) insert/find/erase
- Worst-case O(n) if hashing goes badly
- No lower_bound / upper_bound

### Operations on unordered set

```c++
us.insert(10);    // O(1) avg
us.erase(3);      // O(1) avg
us.find(5);       // O(1) avg
```

### Hashing

- Uses `std::hash<T>` by default
- Works for basic types
- Custom types need a custom hash

```c++
unordered_set<pair<int,int>> us; // ❌ won’t compile
```

- Needs:
  - Custom hash
  - Or lambda hash

## Summary

| Operation | set / multiset | unordered_set |
|-----------|----------------|---------------|
| Insert    | O(log n)       | O(1) avg      |
| Find      | O(log n)       | O(1) avg      |
| Erase     | O(log n)       | O(1) avg      |
| Order     | Sorted         | None          |

- Use **set** when:
  - You need sorted unique elements
  - You need lower_bound / upper_bound
  - Predictable performance matters
- Use **multiset** when:
  - You need sorted data with duplicates
  - Counting occurrences with order
- Use **unordered_set** when:
  - Order doesn’t matter
  - You want fast lookup
