# Pointers

## Pointer Arithematic

```c++
    int A[5]={2,4,6,8,10};
    int *p = A;

    cout<<*p;               => 2

    p++;
    cout<<*p;               => 4

```

Performing incerement/decrement operation doesn't increases the address by one value, but the pointer goes to the next element.

```c++
    int A[5] = {2,4,6,8,10};
    int *p = A;

    cout<<*p;               => 2

    p = p+2;
    cout<<*p;               => 6

        //OR

    cout<<*(p+2);           => 6
```

It points to the p + 2 element.

```c++
    int A[5] = {2,4,6,8,10};
    int *p = &A[0], *q = &A[4];

    cout<< q - p;             => 4
    cout<< p - q;             => -4
```

> Summery : Arithematic operations does not operate on addresses , but on the pointers directly.

## Pointer to a function

```c++
    void Display()
    {
        cout<<"Hello";
    }

    int main()
    {
        void (*fp)();           // Declaration
        fp = Display;           // Initialization
        (*fp)();                // Function Call
    }
```

```c++
    int max(int a, int b)
    {
        return a > b ? a : b;
    }
    int min(int a, int b)
    {
        return a < b ? a : b;
    }

    int main()
    {
        int (*fp)(int, int);

        fp = max;
        (*fp)(10,5);            // Max function will be called

        fp = min;
        (*fp)(10,5);            // Min function will be called
    }
```

## References

Reference is a Alias of variable

- It must be initialised during the declaration
- It doesn’t take any memory
- It cannot be modified to refer other variable
- Syntax for reference declaration is
- `int &y = x;`