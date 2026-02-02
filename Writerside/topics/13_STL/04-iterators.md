# Iterators

Iterator is a pointer to the container.

```c++
vector<int>::iterator it = v.begin(); 
// points to the first element of the vector

for (int i = 0; i < 5; i++)
    cout << *(it + i) << " ";

for (it = v.begin(); it != v.end(); it++)
    cout << *it << " ";
```

There is significant difference between operations on iterators...
- `(it + 1)` points to the next location in the memory
  - `(it + 1)` is useful only when the memory allocation of a container is contiguous, Like in `vectors`
- `(it++)` points to the next element in the container
  - In non-contiguous memory allocated Containers, `(it + 1)` may point to undefined memory.
