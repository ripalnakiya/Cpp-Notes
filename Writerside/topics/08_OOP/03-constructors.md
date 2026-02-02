# Constructors

Constructor is used for initializing an object

- Constructor will have same name as class name
- It will not have a return type
- It is called when object is created
- It can be overloaded
- It can take default arguments
- If it is not defined then class will generate a default constructor

## Types of constructors

- Default constructor (provided by compiler if any constructor is not defined by programmer)
- Non parameterized constructor
- Parameterised constructor
- Copy constructor

```c++
class Rectangle
{
private :
    int length;
    int breadth;

public :
    Rectangle() { // Non parameterised constructor
        length = 1;
        breadth = 1;
    }

    Rectangle(int l, int b) { // Parameterised constructor
        length = l;
        breadth = b;
    }

    Rectangle(int l=1, int b=1) { // Parameterised constructor with default values
        length = l;
        breadth = b;
    }

    Rectangle(Rectangle &rect) { // Copy constructor
        length = rect.length;
        breadth = rect.breadth;
    }
};
```

In copy constructor, argument must be **passed by reference** to avoid infinite recursion.

## Copy Constructor

Copy Constructor is called only when a new object is instantiated.

```c++
Rectangle r1 = Rectangle(5, 10);    // Parameterized Constructor

Rectangle r2(r1);   // Copy Constructor

Rectangle r3 = r1;  // Copy Constructor

Rectangle r4; 
r4 = r1;    // Simply assign all values from one object to another

Rectangle r5;
Rectangle r6 = r5 = r1; // Assign values to r5
                        // Call copy constructor for r6
```

### Shallow Copy

A shallow copy copies the data as-is.

If your class has **pointers**, 
only the pointer value (address) is copied, not what it points to.

Two objects end up pointing to the same memory.

```c++
class Shallow {
public:
    int* data;

    Shallow(int val) {
        data = new int(val);
    }

    // default copy constructor = shallow copy
    // Shallow(Shallow& other) {
    //     data = other.data;      
    // }
    // The adress to which data is pointing to, is copied as it is
};

Shallow a(10);
Shallow b = a;
```

Memory:
```
a.data ----\
             ---> [10]
b.data ----/
```

**Why this is bad ?**

When one object is destroyed:
- Memory gets freed
- The other object still points to it
- Boom: double delete / dangling pointer / undefined behavior

### Deep Copy

A deep copy duplicates the actual data, not just the pointer.

Each object gets its own memory. No sharing.

```c++
class Deep {
public:
    int* data;

    Deep(int val) {
        data = new int(val);
    }

    // Deep copy constructor
    Deep(const Deep& other) {
        data = new int(*other.data);
    }

    ~Deep() {
        delete data;
    }
};

Deep a(10);
Deep b = a;
```

Memory:
```
a.data ---> [10]
b.data ---> [10]
```
