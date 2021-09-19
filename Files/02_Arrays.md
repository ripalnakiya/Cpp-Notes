# Arrays

## for each loop

```cpp
    int A[5] = {2,4,6,8};
    for(int x : A)
        cout << x;              => 2 4 6 8 0
```

This will iterate over each element of the array.

We get copied value from the array (not the reference of the array elements.)

```cpp
    int A[5] = {2,4,6,8};
    for(int x : A)
        cout << ++x;              => 2 4 6 8 0
```

The value of array elements will not be changed.

```cpp
    int A[5] = {2,4,6,8};
    for(int &x : A)
        cout << ++x;              => 3 5 7 9 1
```

Now , the value of array elements will changed because of reference to the array elements.

```cpp
    int A[5] = {2,4,6,8};
    for(auto x : A)
        cout << x;              => 2 4 6 8 0
```

`auto` will determine the datatype of array and change datatype of x accordingly.

### for each loop for 2D arrays

```cpp
    int A[2][3] = {2,4,6,8,10,13};

    for(auto& x : A)
    {
        for(auto& y : x)
        {
            cout<<y<<" ";
        }
        cout<<endl;
    }
```

It is necessary to use & operator with `auto`, because x is a row of the array.

But for y we can use int as well, since it is a element of the array(row).

```cpp
    int A[2][3] = {2,4,6,8,10,13};

    for(auto& x : A)
    {
        for(int y : x)
        {
            cout<<y<<" ";
        }
        cout<<endl;
    }
```
