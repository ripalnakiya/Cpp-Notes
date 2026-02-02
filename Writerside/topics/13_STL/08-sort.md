# Sort

## sort

```c++
#include <algorithm>
std::sort(begin, end);
```

**What algorithm does `std::sort` use?** Introsort

Introsort =
- Quicksort (fast on average)
- Heapsort (safe worst-case)
- Insertion sort (tiny ranges)

### Complexity

| Case    | Time       | Space    |
|---------|------------|----------|
| Best    | O(n log n) | O(log n) |
| Average | O(n log n) | O(log n) |
| Worst   | O(n log n) | O(log n) |

### Stability

- ❌ Not stable
- Equal elements may reorder

## stable sort

```c++
std::stable_sort(begin, end);
```

What it uses
- Typically merge sort
- Guaranteed stability

Complexity
- Time: O(n log n)
- Space: O(n)
