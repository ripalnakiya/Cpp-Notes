# Templates
<show-structure depth="2"/>

Templates are blueprints for code.

We write logic once, 
and C++ generates versions of it for different data types at compile time.

**Let's look at the problem we had:**

```c++
int square(int x) {
    return x * x;
}

float square(float x) {
    return x * x;
}
```

We had to write same code for different data type, multiple times...

Previous two functions can be replaced with one:

```c++
template <typename T>
T square(T x) {
    return x * x;
}

```

Usage:
```c++
square<int>(2);        // T = int
square<double>(2.5);   // T = double
```

The compiler internally generates:
```c++
int square(int);
double square(double);
```

> We can use `class` instead of `typename`
> 
> `T` is a type placeholder, We can write `Foo` as well
{style="note"}

## Template Function

- Function template are used for defining "generic functions"
- They work for multiple datatypes
- Datatype is decided based on the type of value passed
- Datatype is a template variable

```c++
template <typename T>
T maximum(T x, T y)
{
    return (x > y) ? x : y;
}

template <typename T, typename U>
U add(T x, U y) // we have set "return type" to "type" of the second parameter
{
    return (x + y);
}

int main()
{
    cout << maximum(5, 10) << endl; // 10
    cout << add(5, 10.2) << endl; // 15.2
    return 0;
}
```

### How the compiler decides `T` (type deduction)

Case 1: Automatic deduction
```c++
max(3, 5);       // T = int
max(2.1, 4.7);   // T = double
```

Case 2: Explicit type
```c++
max<int>(3, 5);
```

### Template functions are type-strict

```c++
max(3, 4.5);
```

This will not compile. **Why ?**

Because C++ refuses to guess whether:
- `T` should be `int`
- `T` should be `double`

Templates do not do implicit type mixing.

**Fix:**
```c++
max<double>(3, 4.5);

// OR

max(3.0, 4.5);
```

### Multiple template parameters

```c++
template <typename T, typename U>
auto add(T a, U b) {
    return a + b;
}
```

Usage:
```c++
add(3, 4.5);   // T=int, U=double → returns double
```

- `T` and `U` can be different
- `auto` lets the compiler deduce the return type

### When template functions are instantiated ?

Templates are generated:
- Only when used
- For each unique type

```c++
square(5);       // generates square<int>
square(5);       // reused
square(2.0);     // generates square<double>
```

No runtime overhead.
Just extra compiled code.

Trade-off:
- Faster execution
- Larger binary

### Templates should support the operators

```c++
template <typename T>
T bigger(T a, T b) {
    return (a > b) ? a : b;
}
```

This works, only if `T` supports: `operator>`

If not, compilation fails.

## Template Class

Templates can work for any data type.

**Program 1 : `int` specific class for Stack**

```c++
class Stack
{
    int* stackPtr;
    int top;
    int size;

public:
    Stack(int size)
    {
        this->size = size;
        top = -1;
        stackPtr = new int[size];
    }
    void push(int x);
    int pop();
};

void Stack::push(int x) {
    if (top == size - 1)
        cout << "Stack is Full";
    else {
        top++;
        stackPtr[top] = x;
    }
}

int Stack::pop() {
    int x = 0;
    if (top == -1)
        cout << "Stack is Empty" << endl;
    else {
        x = stackPtr[top];
        top--;
    }
    return x;
}

int main() {
    Stack s(10);
    s.push(10);
    s.push(23);
    s.push(33);
}
```

**Program 2 : Generic class for Stack**

```c++
template <typename T>
class Stack
{
    T* stackPtr;
    int top;
    int size;

public:
    Stack(int size)
    {
        this->size = size;
        top = -1;
        stk = new T[size];
    }
    void push(T x);
    T pop();
};

template <typename T>
void Stack<T>::push(T x) {
    if (top == size - 1)
        cout << "Stack is Full";
    else {
        top++;
        stackPtr[top] = x;
    }
}

template <typename T>
T Stack<T>::pop() {
    T x = 0;
    if (top == -1)
        cout << "Stack is Empty" << endl;
    else {
        x = stackPtr[top];
        top--;
    }
    return x;
}

int main() {
    Stack<int> s(10);
    s.push(10);
    s.push(23);
    s.push(33);
    
    Stack<float> s(10.0f);
    s.push(10.0f);
    s.push(23.0f);
    s.push(33.0f);
}
```

The compiler generates separate classes for `int` and `float` internally.
