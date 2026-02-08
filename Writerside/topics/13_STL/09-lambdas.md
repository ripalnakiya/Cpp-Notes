# Lambdas
<show-structure depth="2"/>

They are inline functions which can be used for short snippets of code 
that are not going to be reused and therefore do not require a name.

```c++
void main()
{
    [] () {cout<<"Hello"<<endl;} ();       => Hello
}
```

## Syntax

```c++
[capture](parameters) -> return_type {
    body
};
```


## Parameters and return type

```c++
[](int a, int b) { return a + b; }
```

Return type is usually inferred.

- But required if:
  - Multiple return paths
  - Confusing types

```c++
[](int x) -> double {
    if (x > 0) return x * 1.5;
    return 0.0;
};
```

## Usage

```c++
void main()
{
    int sum = [] (int a, int b) {return a+b;} (10, 20);
    cout<<sum;      // 30                                                              
}
```

```c++
void main()
{
    // Assigning the function reference to a pointer
    auto f = [] () {cout << "Hello World" << endl;};
    f();            // Hello World                                                                
}
```

## Capture List

The capture list decides what outside variables the lambda can see and how.

**1. Capture nothing**
```c++
[]() {
    cout << "No outside access";
};
```

**2. Capture by value**
```c++
int x = 10;

auto f = [x]() {
    cout << x;
};
```

```c++
int main()
{
    int a = 10;

    auto f = [a] () {cout << a << endl;};       // statement 1

    f();                                        => 10
    a++;
    f();                                        => 10
}
```

The value of `a` is replaced at the definition of the lambda expression, 
hence it does not access the latest/updated value of `a`, but the original copied value of a.

Moreover, Here we **cannot modify the value of captured variables** inside the lambda expression.

Capture by value variables are read-only.

**3. Capture by reference**
```c++
int x = 10;

auto f = [&x]() {
    x++;
};
```

- Refers to the original variable

```c++
int main()
{
    int a = 10;

    auto f = [&a] () {cout << ++a << endl;};

    f();                                        => 11
    ++a;
    f();                                        => 13
}
```

**4. Capture everything**
```c++
[=]  // all by value
[&]  // all by reference
```

**5. Mixed capture**
```c++
[x, &y]()
```

## Lambdas vs function pointers

```c++
int (*fp)(int, int);

auto lambda = [](int a, int b) { return a + b; };
```

Lambdas without captures ✅ can be converted to function pointers.

```c++
int (*fp)(int, int) = [](int a, int b) {
    return a + b;
};
```

## Internal Implementation

A lambda is an unnamed function object.

```c++
auto add = [](int a, int b) {
    return a + b;
};
```

- It creates:
  - A compiler-generated class
  - With an overloaded `operator()`

```c++
// So, this
add(2, 3);

// is really:
add.operator()(2, 3);
```
