# Maps
<show-structure depth="2"/>

## Map

```c++
std::map<Key, Value>

map<int, string> mp;
mp[3] = "three";
mp[1] = "one";
mp[2] = "two";

// Stored as:
1 → one
2 → two
3 → three
```

- Stores unique keys
- Keys are sorted
- Implemented using a Red-Black Tree
- Keys are **immutable**

Elements stored as:
```c++
pair<const Key, Value>
```

### Access methods

**`operator[]`**

```c++
mp[5] = "five";
```

- If key 5 does not exist:
  - It gets inserted
  - Value is default-constructed

**`at()`**

```c++
mp.at(3);
```

- Throws exception if key not found
- Does not insert

### Operations on map

```c++
mp.insert({4, "four"});   // O(log n)
mp.erase(2);              // O(log n)
mp.find(3);               // O(log n)
mp.count(3);              // 0 or 1 | O(log n)
```

### Iteration

```c++
for (auto &p : mp) {
    cout << p.first << " " << p.second;
}
```

Always in sorted key order.

### Lower and upper bound on map

```c++
auto it = mp.lower_bound(3); // pointer to first key that is >= 3
auto it2 = mp.upper_bound(5); // pointer to first key that is > 5
```

Used in **Range queries**.

## Multimap

```c++
std::multimap<Key, Value>

multimap<int, string> mm;
mm.insert({1, "a"});
mm.insert({1, "b"});

// Stored as:
1 → a
1 → b
```

- Same as map
- Allows duplicate keys
- Still sorted
- Still tree-based

### Map vs Multimap

| Feature        | map | multimap |
|----------------|-----|----------|
| Duplicate keys | ❌   | ✅        |
| operator[]     | ✅   | ❌        |
| Sorted         | ✅   | ✅        |

No `[]` operator in `multimap`.
Because which value would it return? Exactly.

### Accessing all values for a key

```c++
auto range = mm.equal_range(1);
for (auto it = range.first; it != range.second; it++) {
    cout << it->second;
}
```

### Erase behavior

```c++
mm.erase(1); // removes ALL entries with key 1

// Erase one
auto it = mm.find(1);
mm.erase(it);
```

## Unordered Map

```c++
std::unordered_map<Key, Value>

unordered_map<int, string> ump;
ump[3] = "three";
ump[1] = "one";

// Iteration order: Undefined.
??? → ???
```

- Stores unique keys
- No ordering
- Implemented using a hash table
- Faster on average

### No range queries

- You do not get:
  - `lower_bound`
  - `upper_bound`
  - Sorted iteration

### Hashing

- Built-in types works
- Custom keys need a custom hash

```c++
unordered_map<pair<int,int>, int> mp; // ❌
```

## Summary

| Operation | map / multimap | unordered_map |
|-----------|----------------|---------------|
| Insert    | O(log n)       | O(1) avg      |
| Find      | O(log n)       | O(1) avg      |
| Erase     | O(log n)       | O(1) avg      |
| Order     | Sorted         | None          |

- Use **map** when:
  - You need sorted keys
  - You need range queries
  - Deterministic iteration order matters
- Use **multimap** when:
  - One key maps to multiple values
  - Order matters
  - Duplicates are intentional
- Use **unordered_map** when:
  - Order doesn’t matter
  - Performance is critical
