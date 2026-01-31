# Object Oriented Programming

Features

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

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
    Rectangle *r = new Rectangle();     // with () or without () works the same way.
    q->length = 20;
    q->breadth = 30;
}
```

## Member Function Declaration

```c++
class Rectangle
{
    public :
        int length;
        int breadth;

        int perimeter()                        // Declaration and Definition inside the class
        {
            return 2 * (length + breadth);
        }
        int area();                             // Declaration in class
};

int Rectangle::area()                           // Defining outside the class using scope resolution operator
{
    return length*breadth;
}

int main()
{
    Rectangle r1;
    r1.length = 10;
    r2.breadth = 5;
    cout<< r1.perimeter() <<endl;               // Code of perimeter() will be copied here.
    cout<< r1.area() <<endl;
    return 0;
}
```

The classes which are defined inside the class are `inline` functions by default.

`inline` functions are copied in the main function at the place of function call.

This increases the compiler overhead of copying and pasting the `inline` functions and making the main function/source code larger.

The classes which are defined outside the class are `Non inline` functions.

> **Note** : To make a function, which is defined outside the class, `inline` we can use `inline` keyword at function declaration.
>
> ```c++
> inline int area();
> ```

## Types of member functions

- Constructors - called when object is created
- Accessors - used for knowing the value of data members
- Mutators - used for changing value of data member
- Facilitator - actual functions of class
- Enquiry - used for checking if an object satisfies some condition
- Destructor - used for releasing resources used by object

### Accessors and Mutators

By rules, we should not access the data members of class directly.
Instead, we should use accessors and mutators to deal with the data members.

- Data members of a class class are usually declared as Private or Protected
- They can be accessed only inside the class and child classes
- Data hiding protects data from mishandling

```c++
class Rectangle
{
    private :
        int length;
        int breadth;

    public :
        void setLength(int l)               // Mutator
        {
            length = l;
        }

        void setBreadth(int b)              // Mutator
        {
            breadth = b;
        }

        int getLength()                     // Accessor
        {
            return length;
        }

        int getBreadth()                    // Accessor
        {
            return breadth;
        }

        int perimeter()                     // Facilitator
        {
            return 2 * (length + breadth);
        }

        int area()                          // Facilitator
        {
            return length*breadth;
        }
};
```

### Constructors

Constructor will have same name as class name

Constructor will not have return type

Constructor should be public

Constructor can be declared as private also in some cases

Constructor is called when object is created

Constructor is used for initialising an object

Constructor can be overloaded

Constructor can take default arguments

If it is not defined then class will have a default constructor

- Types of constructor

  - Default constructor (provided by compiler if any constructor is not defined by programmer)
  - Non parameterised constructor
  - Parameterised constructor
  - Copy constructor

```c++
class Rectangle
{
    private :
        int length;
        int breadth;

    public :
        Rectangle()                 // Non parameterised constructor
        {
            length = 1;
            breadth = 1;
        }

        Rectangle(int l, int b)     // Parameterised constructor
        {
            length = l;
            breadth = b;
        }

        Rectangle(int l=1, int b=1)     // Parameterised constructor with default values
        {
            length = l;
            breadth = b;
        }

        Rectangle(Rectangle &rect)      // Copy constructor
        {
            length = rect.length;
            breadth = rect.breadth;
        }

        int perimeter()
        {
            return 2 * (length + breadth);
        }

        int area()
        {
            return length*breadth;
        }
};
```

### Shallow and Deep Copy Constructor

Shallow Copy constructor

```c++
class Test
{
    public:
        int a;
        int *p;

        Test(int x)
        {
            a = x;
            p = new int[a];
        }

        Test(Test &t)
        {
            a = t.a;
            p = t.p;    // This will point to the heap memory , where the t1 object is pointing.
                        // This will not create a new heap memory for the calling object.
        }
}

int main()
{
    Test t1(5);
    Test t2(t1);
    return 0;
}
```

Deep Copy Constructor

```c++
class Test
{
    public:
        int a;
        int *p;

        Test(int x)
        {
            a = x;
            p = new int[a];
        }

        Test(Test &t)
        {
            a = t.a;
            p = new int[a];     // This will create a sperate heap, for the calling object
        }
}

int main()
{
    Test t1(5);
    Test t2(t1);
    return 0;
}
```

### Summary

```c++
class Rectangle
{
    private:
        int length;
        int breadth;
    public:
        Rectangle();                        // Non Parameterized constructor
        Rectangle(int l,int b);             // Parameterized constructor
        Rectangle(Rectangle &r);            // Copy constructor
        int getLength(){return length;}     // Accessor (Inline function)
        int getBreadth(){return breadth;}   // Accessor (Inline function)
        void setLength(int l);              // Mutator
        void setBreadth(int b);             // Mutator
        int area();                         // Facilitator
        int perimeter();                    // Facilitator
        bool isSquare();                    // Enquiry function
        ~Rectangle();                       // Destructor
};

int main()
{
    Rectangle r1(10,10);
    cout<<"Area "<<r1.area()<<endl;
    if(r1.isSquare())
        cout<<"Yes"<<endl;
    return 0;
}

Rectangle::Rectangle()
{
    length=1;
    breadth=1;
}
Rectangle::Rectangle(int l,int b)
{
    length=l;
    breadth=b;
}
Rectangle::Rectangle(Rectangle &r)
{
    length=r.length;
    breadth=r.breadth;
}
void Rectangle::setLength(int l)
{
    length=l;
}
void Rectangle::setBreadth(int b)
{
    breadth=b;
}
int Rectangle::area()
{
    return length*breadth;
}
int Rectangle::perimeter()
{
    return 2*(length+breadth);
}
bool Rectangle::isSquare()
{
    return length==breadth;
}
Rectangle::~Rectangle()
{
    cout<<"Rectangle Destroyed";
}
```