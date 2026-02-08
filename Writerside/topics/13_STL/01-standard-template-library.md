# Standard Template Library
<show-structure depth="2"/>

- STL is a collection of generic classes and functions that give you:
  - Ready-made data structures
  - Algorithms to work on them
  - Iterators to glue everything together

- All of this is:
  - Type-safe
  - Fast (usually very fast)
  - Battle-tested by decades of human suffering

## Containers

They store data.

### Sequence containers (ordered by insertion)

- `vector`: Dynamic array. Lives in contiguous memory.
  - Access: O(1)
  - Insert at end: amortized O(1)
  - Insert in middle: O(n)
- `deque` : Double-ended queue. Fast insert/remove at both ends.
  - Access: O(1)
  - Ends: O(1)
- `list` : Doubly linked list.
  - Insert/delete anywhere: O(1)
  - Access: O(n)

### Associative containers (sorted, tree-based)

 - `set` / `map`
   - Implemented using Red-Black Trees.
   - Elements are always sorted.
   - No duplicates in set, unique keys in map.
   - Insert/search/delete: O(log n)

- `multiset` / `multimap` : Same thing, but duplicates allowed.

### Unordered containers (hash-based)

- `unordered_set` / `unordered_map`
  - No order.
  - Uses hashing.
  - Average: O(1)
  - Worst-case: O(n)

Use these when order doesn’t matter and speed does.

### Container adapters (restricted interfaces)

- `stack` → LIFO
- `queue` → FIFO
- `priority_queue` → Heap (max-heap by default)

## Iterators

They let algorithms work on containers without caring what container it is.

- Types:
  - Input
  - Output
  - Forward
  - Bidirectional
  - Random-access (vector, deque)

```c++
for (auto it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";
}
```

## Algorithms

Containers hold data, algorithms manipulate it.

- Some classics:
  - `sort()`
  - `reverse()`
  - `binary_search()`
  - `find()`
  - `count()`
  - `max_element()`

```c++
sort(v.begin(), v.end());
```

Algorithms do not belong to containers

They work on iterator ranges

## Functors and Lambdas

Algorithms can take custom behavior.

```c++
sort(v.begin(), v.end(), [](int a, int b) {
    return a > b;
});
```
