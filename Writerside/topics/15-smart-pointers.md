# Smart Pointers

They automatically deallocate the heap memory, when objects goes out of scope.

**Why smart pointers exist ?** Raw pointers don’t own anything. They just point, while we:
- forget to delete
- delete twice
- delete too early
- delete too late
- delete the wrong thing

## Base Problem

```c++
void fun()
{
    Rectangle *p = new Rectangle();
}

void main()
{
    fun();
}
```

When function `fun()` is finished executing,

Pointer `p` is deleted from the activation record of the function.

But the value allocated in the **heap memory is not released**.

(It does not deallocate the object, when it goes out of scope)

There is wastage of memory.

To solve this problem,
we need to delete the memory explicitly using `delete` keyword.

```c++
void fun()
{
    Rectangle *p = new Rectangle();
    delete p;
}

void main()
{
    fun();
}
```

This solves the problem.

## Usage of smart pointer

```c++
#include <memory>

void fun()
{
    unique_ptr<Rectangle> p = make_unique<Rectangle>();
    cout << p->area();
    cout << p->perimeter();
}

int main()
{
    fun();
}
```

The `unique_ptr` class will delete the pointer as well as deallocate the memory,
when the pointer goes out of scope.

So, we don't have to worry about deallocating the heap memory.

## Types of Smart Pointers

## 1. unique_ptr

A resource can be pointed by exactly one pointer.

Properties:
- Exclusive ownership
- Cannot be copied
- Can be moved
- Zero overhead compared to raw pointer
- Best default choice

```c++
unique_ptr<int> p1 = make_unique<int>(10);

// std::unique_ptr<int> p2 = p1; ❌ compilation error

unique_ptr<int> p2 = move(p1); // ownership transferred
```

After `move`:
- `p2` owns the memory
- `p1` becomes `nullptr`
- No memory leak, no double delete

## 2. shared_ptr

More than one pointer can point to the same resource.

A `shared_ptr` keeps a reference count. 
The object is destroyed when the count reaches zero.

```c++
std::shared_ptr<int> p1 = std::make_shared<int>(42);
std::shared_ptr<int> p2 = p1;
std::shared_ptr<int> p3 = p2;
```

Reference count: 3

When `p1`, `p2`, and `p3` all die, the object dies too.

```c++
p.use_count(); // for debugging, returns the reference count
```

## 3. weak_ptr

It is almost same as `shared_ptr`. 

More than one pointer can point to the same object.

**The problem:** `shared_ptr` can leak without leaking memory.

```c++
struct A {
    shared_ptr<B> b;
};

struct B {
    shared_ptr<A> a;
};
```

A owns B, B owns A. Reference count never reaches zero.

A `weak_ptr`:
- Does NOT increase reference count
- Does NOT own the object
- Can observe safely
- Useful to avoid deadlock
