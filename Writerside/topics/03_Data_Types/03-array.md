# Array
<show-structure depth="2"/>

Declaration:

```c++
type array_name[size];

int arr[10];    // Will allocate memory for 10 elements
                // and will have garbage values

// Initialisze the array
for (int i = 0; i < 10; i++)
    arr[i] = i;
```

Declaration and Initialisation:
```c++
int arr[10] = {2, 7, 9, 14, 17}; 
// Remaining elements will be filled to with 0
```

## Range based loop

```c++
    int A[5] = {2,4,6,8};
    for(int x : A)
        cout << x;              => 2 4 6 8 0
```

We get copied value from the array (not the reference of the array elements.)


```c++
    int A[5] = {2,4,6,8};
    for(int &x : A)
        cout << ++x;              => 3 5 7 9 1
```

Now , the value of array elements will changed because of reference to the array elements.

```c++
    int A[5] = {2,4,6,8};
    for(auto x : A)
        cout << x;              => 2 4 6 8 0
```

`auto` will determine the datatype of array and change datatype of `x` accordingly.

### Range based loop for 2D arrays

```c++
    int A[2][3] = {2,4,6,8,10,13};

    for(auto& x : A)
    {
        for(auto& y : x)
        {
            cout << y << " ";
        }
        cout << endl;
    }
```

It is necessary to use `&` operator with `auto`, because `x` is a row of the array.

But for `y` we can use `int` as well, since it's just an element of the array(row).
