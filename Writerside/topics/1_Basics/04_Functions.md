# Functions

- Functions can return a single value
- Default return type is `int`

## Function Overloading

- If More than one functions can have same name, but different parameter list, then they are overloaded functions
- Return the is not considered in overloading
- Function overloading is used for achieving compile time polymorphism

## Function Template

- Function template are used for defining "generic functions"
- They work for multiple datatypes
- Datatype is decided based on the type of value passed
- Datatype is a template variable
- Function can have multiple template variables

```c++
    template <class T>
    T maxi(T x, T y)
    {
        return (x > y) ? x : y;
    }

    template <class T, class U>
    U add(T x, U y)     // we have set return "type" to "type" of second parameter
    {
        return (x + y);
    }

    int main()
    {
        cout << maxi(5, 10) << endl;            => 10
        cout << add(5, 10.2) << endl;           => 15.2
        return 0;
    }
```

## Returning from a function

### Return by Address

- A function can return address of memory
- It should not return address of local variables, which will be disposed after function ends
- It can return address of memory allocated in heap

```c++
    int * fun(int n)
    {
        int *p = new int[n];
        for(int i=0; i<n; i++)
            p[i] = i + 1;
        return p;
    }

    int main()
    {
        int *ptr = fun(5);
        for(int i=0; i<5; i++)
            cout<<i<<endl;
        return 0;
    }
```

### Return by Reference

- It should not return reference of its local variables
- It is written on left side of the assignment operator

```c++
    int& min(int &a, int &b)
    {
        if(a < b)
            return a;
        else
            return b;
    }

    int main()
    {
        int a=10, b=20;
        min(a,b) = 0;
        cout<<a;                    => 0
        cout<<b;                    => 20
    }
```

## Static Variables

- They have local scope but remain in memory through out the execution of program
- They are created in code section
- They are history-sensitive

```c++
    void fun()
    {
        static int v=0;
        int a=10;
        v++:
        cout<<a<<“ “<<v;
    }
    int main()
    {
        fun();              => 10 1
        fun();              => 10 2
        fun();              => 10 3
    }
```