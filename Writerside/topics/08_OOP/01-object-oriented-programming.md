# Object Oriented Programming

Features

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism
- Modularity

## Class and Object

```c++
class Rectangle
{
    public :
        int length;
        int breadth;

        int perimeter()
        {
            return 2 * (length + breadth);
        }

        int area()
        {
            return length*breadth;
        }
};

int main()
{
    // Creating object in stack
    Rectangle r1;
    r1.length = 10;
    r1.breadth = 20;

    // Accessing object properties/methods using pointer
    Rectangle *p = &r1;
    p->length = 15;
    p->breadth = 25;

    // Creating object in heap
    Rectangle *q = new Rectangle;
    Rectangle *r = new Rectangle(); // with () or without () works the same way
    q->length = 20;
    q->breadth = 30;
}
```

## Access Specifiers

### private

The default for classes.

- Members are accessible only inside the same class
- Not accessible from:
  - Objects
  - Derived classes
  - Outside functions
  - nested classes
  - enclosing classes

### public

- Members are accessible from anywhere
- Objects, functions, other classes, everyone can access it

### protected

- Accessible:
  - Inside the class
  - Inside derived (child) classes
- Not accessible from 
  - objects
  - non-derived code
  - nested classes
  - enclosing classes

| Access Specifier | Same Class | Derived Class | Outside Code |
|------------------|------------|---------------|--------------|
| `private`        | ✅          | ❌             | ❌            |
| `protected`      | ✅          | ✅             | ❌            |
| `public`         | ✅          | ✅             | ✅            |

## Member Function Declaration

```c++
class Rectangle
{
    public :
        int length;
        int breadth;

        int perimeter() // Declaration and Definition inside the class
        {
            return 2 * (length + breadth);
        }
        int area(); // Declaration in class
};

int Rectangle::area() // Defining outside the class using scope resolution operator
{
    return length*breadth;
}

int main()
{
    Rectangle r1;
    r1.length = 10;
    r2.breadth = 5;
    cout<< r1.perimeter(); // Code of perimeter() will be copied here.
    cout<< r1.area();
    return 0;
}
```

The classes which are defined inside the class are `inline` functions by default.

> `inline` functions are copied in the main function at the place of function call.
>
> This increases the compiler overhead of copying and pasting the `inline` functions and making the main function/source code larger.

The functions which are defined outside the class are `non inline` functions.

> To make a function, which is defined outside the class, `inline` we can use `inline` keyword at function declaration.
>
> `inline int area();`

## Types of member functions

- Constructors - called when object is created
- Accessors - used for knowing the value of data members
- Mutators - used for changing value of data member
- Facilitator - actual functions of class
- Enquiry - used for checking if an object satisfies some condition
- Destructor - used for releasing resources used by object

### Accessors and Mutators

By standards, we should not access the data members of class directly.
Instead, we should use accessors and mutators to deal with the data members.

- Data members of a class are usually declared as Private or Protected
- They can be accessed only inside the class and child classes

```c++
class Rectangle
{
    private :
        int length;
        int breadth;

    public :
        void setLength(int l) { // Mutator
            length = l;
        }
        void setBreadth(int b) { // Mutator
            breadth = b;
        }
        int getLength() { // Accessor
            return length;
        }
        int getBreadth() { // Accessor
            return breadth;
        }
        int perimeter() { // Facilitator
            return 2 * (length + breadth);
        }
        int area() { // Facilitator
            return length*breadth;
        }
};
```

## this pointer

`this` is an implicit pointer available inside non-static member functions of a class.

It points to the current object that called the function.

**Used for:**

### 1. Disambiguation

```c++
class Person {
    int age;

public:
    void setAge(int age) {
        this->age = age;
    }
};
```

**Why to use `this`?**

Because the parameter `age` shadows the data member `age`.

Without `this`:
```c++
age = age;   // congratulations, you assigned the parameter to itself
```

With `this`:
```c++
this->age = age;  // member = parameter
```

### 2. Return current object

```c++
class Counter {
    int value = 0;

public:
    Counter* increment() {  // returning pointer of object
        value++;
        return this;
    }
};

// Usage:
Counter c;
c.increment()->increment()->increment();
```

```c++
class Counter {
    int value = 0;

public:
    Counter& increment() {  // returning a reference of object
        value++;
        return *this;
    }
};

// Usage:
Counter c;
c.increment().increment().increment();
```
> `friend` functions are not member functions of class, 
> so they can't access `this` pointer
