# Table of Contents

[1. Basics](#basics)

[2. Arrays](#arrays)

[3. Pointers](#pointers)

[4. Functions](#functions)

[5. Object Oriented Programming](#object-oriented-programming)

[6. Operator Overloaing](#operator-overloading)

[7. Inheritance](#inheritance)

[8. Polymorphism](#polymorphism)

[9. Friend and Static Members](#friend-and-static-members)

[10. Exception Handling](#exception-handling)

[11. Template Classes](#template-classes)

[12. Constants Preprocessors and Namespaces](#constants-preprocessors-and-namespaces)

[13. Destructors](#destructors)

[14. IO Stream](#iostream)

[15. Standard Template Library](#standard-template-library)

[16. C++11](#cpp11)

# Basics

## Theory

### Compiler vs Interpreter

- Compilation of source code is done only once
- Compiler generates a separate executable(.exe) file
- Translation of source code to machine code is done only once, so we don't compiler to excute our program.
- The compiled program are fast because they gets executed independently.
- Language is easy (program doesn't executes if there's single error)

- It translates the source code into machine code line by line, and then excutes the line
- We need browser/Interpreter every time we want to run the code. (Translation happens every time we want to run the code)
- Interpreted programs are slow because they get executed inside the interpreter
- Language is difficult (program executes until the error is encountered)

### Programming Paradigm

- Monolothic Programming (single file - entire program)
- Procedural/Modular/Functional Programming (Breaking the program into functions : C language)
- Object Oriented Programming (C++ language)

---

## Basic Concepts

### Datatypes

- Int data type range (Assuming 2 bytes)
  bits : 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

  MSB is used to represent sign of the number
  0 for positive, 1 for negative

  we're remaining with 15 bits to represent the number

  so, 2^15 = 32768

  - 0 | 0 to 32767 (positive numbers)
  - 1 | 0 to 32767 (negative numbers)
    since, there can't be -0, so considering upto -32768.

- Char data type range (1 byte)
  bits : 8 7 6 5 4 3 2 1 0

  we know, 2^7 = 128

  - 0 | 0 to 127 (positive numbers)
  - 1 | 0 to 127 (negative numbers)
    since, there can't be -0, so considering upto -128

> **Note:** Negative numbers are always stored in 2's complement
>
> for example, 12 = 0000000000001100
>
> -12 : 12's 1's complement = 1111111111110011 : add 1 to it = 1111111111110100
>
> -12 = 1111111111110100
>
> For viewing decimal of a binary negative number (e.g. 1111111111110100)
>
> we has to find 2's complement of this number and then convert it to decimal and then add -ve sign.

### Data type modifiers

- usigned (can only be used with int and char)

  `unsigned int` will have range 0 to 65535 , since It won't contain any negative numbers (only positive numbers)

  we know, 2^16 = 65536

  `unsigned chat` will have range 0 to 255, since it won't contain any negative numbers (only positive numbers)

  we know, 2^8 = 256

- long (cannot be used with char)

  `long int` will have size 4 bytes (Initially 2 bytes)

  `long float` will have size 8 bytes (Initially 4 bytes)

  `long double` will have size 10/16 bytes (Initially 8 bytes)

  > **Note:** : long float = double , so no need to use long float

### Initialization

These are different ways to initialize int

```cpp
    int day = 1;
    int day(1);
    int day = (1);
    int day {1};
    int day = {1};
```

### Literals

```cpp
    int a = 10;
    int a = 010; // Octal representation if 8
    int a = 0x41; // Hexadecimal representation of 65
```

> **Note:** : the calculations will happen in decimal system only , by default

```cpp
    long price = 65359L;
    float price = 12.5F;
```

```cpp
    char section = 'A';
    char section = 65;
```

#### Coersion

If a value is converted to required datatype internally, then it is called coersion.

```cpp
    char x = 65.6;          => A
```

```cpp
    float x = 123.45F;        => 123.45
```

```cpp
    float x = 123e2F;       => 12300
```

```cpp
    float x = 123e-2F;       => 1.23
```

### Operators and Expressions

If two integers are divided then, the result will also be of the integer type;

```cpp
    int a=13, b=5,c;
    c = a/b;                => 2
```

To get original result

```cpp
    int a=13, b=5;
    float c;                                    // c should hold the float value
    c = (float) a/b;             => 2.6         // Implicit type casting

```

```cpp
    int a=13;
    float c;
    c = a / 5.0;                => 2.6
```

> **Note:** : % operator can be performed on "int" and "char" , but not on "float"

#### Compound Assignment

```cpp
    sum = sum + a + b + c;
```

is same as the following

```cpp
    sum += a + b + c;
```

### Overflow

When the datatype value is increased by its limit, then it will overflow
and the result will be in cyclic order. (-128 | 0 | 127)

```cpp
    char b=127;
    b++;
    cout<<(int)b<<endl;         => -128 //since 128 value doesn't exist for char
```

```cpp
    char d=-128;
    d--;
    cout<<(int)d<<endl;         => 127 //since -129 value doesn't exist for char
```

### Left shift and right shift

```cpp
    char a=5, b, i=1;
    b = j<<i; // left shift by 1
    cout<<(int)b<<endl;            => 10 // value is a*(2^i)
```

```cpp
    char a=20, b, i=1;
    b = a>>1; // right shift by 1
    cout<<(int)m<<endl;             => 10 // value is a/(2^i)
```

> **Note:** : signed bits are not disturbed in the shift operation

### Enum and typedef (user defined data types)

```cpp
               0    1    2    3    4    5   6
    enum day {mon, tue, wed, thu, fri, sat, sun};
    day d = mon;    // d will get value 0;
```

```cpp
                      2    3    4     5   6    7
    enum day {mon=1, tue, wed, thu, fri, sat, sun};
```

```cpp
                      2           6    7          10
    enum day {mon=1, tue, wed=5, thu, fri, sa=9, sun};
```

```cpp
    typedef int marks;
    marks m1, m2, m3;
```

---

## Conditional Statements

### Dynamic Declaration

This method is not memory efficient because it is declared in the main function and will occupy the memory until the program terminates(main function gets over).

```cpp
    int c = a + b;
    if (c > 10) {
        // do something
    }
```

This approach is better , that declare a variable inside a simple block and then the do processing.

After the block is finished executing, the memory allocated to the variable will be deleted.

```cpp
    {
        int c = a + b;
        if (c > 10)
        {
            // do something
        }
    }
```

This feature was introduced in C++17 , and it works exactly same as previous approach.

```cpp
    if(int c = a + b; c > 10)
    {
        // do something
    }
```

Another way to use this feature

```cpp
    if(int e=a*b)
    {
        cout<<e<<endl;
    }
```

There is declaration and assignment in the if condition, which will return true and the block will get executed.

The memory allocated to the variable will be deleted after the block is finished executing.

### Switch case - Branch and control statement

Switch cases are faster than if else ladder.

We can write the default anywhere inside the switch block.

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

## for each loop for 2D arrays

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

---

# Pointers

## Pointer Arithematic

```cpp
    int A[5]={2,4,6,8,10};
    int *p = A;

    cout<<*p;               => 2

    p++;
    cout<<*p;               => 4

```

Performing incerement/decrement operation doesn't increases the address by one value, but the pointer goes to the next element.

```cpp
    int A[5] = {2,4,6,8,10};
    int *p = A;

    cout<<*p;               => 2

    p = p+2;
    cout<<*p;               => 6

        //OR

    cout<<*(p+2);           => 6
```

It points to the p + 2 element.

```cpp
    int A[5] = {2,4,6,8,10};
    int *p = &A[0], *q = &A[4];

    cout<< q - p;             => 4
    cout<< p - q;             => -4
```

> Summery : Arithematic operations does not operate on addresses , but on the pointers directly.

## Pointer to a function

```cpp
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

```cpp
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

---

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

```cpp
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

```cpp
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

```cpp
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

```cpp
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

# Object Oriented Programming

Features

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

## Class and Object

```cpp
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

```cpp
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
> ```cpp
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

```cpp
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

```cpp
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

```cpp
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

```cpp
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

```cpp
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

# Operator Overloading

We can define operator for our own classes.

Operators can be overloaded using member functions or friend functions.

Global functions can also access private and protected members of an object if they are
declared as friend inside a class.

First, let us see basic function

```cpp
class Complex
{
public:
    int real;
    int imag;

    Complex(int real = 0, int imag = 0)
    {
        this->real = real;
        this->imag = imag;
    }

    Complex add(Complex c)
    {
        Complex temp;
        temp.real = this->real + c.real;
        temp.imag = this->imag + c.imag;
        return temp;
    }
};

void main()
{
    Complex c1(10, 5), c2(2, 2), c3;
    c3 = c1.add(c2);
//  c3 = c2.add(c1);                                This would also give the same result
    cout << c3.real << "+i" << c3.imag << endl;     => 12+i7
}
```

Now let us see how operators are overloaded.

```cpp
class Complex
{
public:
    int real;
    int imag;

    Complex(int real = 0, int imag = 0)
    {
        this->real = real;
        this->imag = imag;
    }

    Complex operator+(Complex c)
    {
        Complex temp;
        temp.real = this->real + c.real;
        temp.imag = this->imag + c.imag;
        return temp;
    }
};

void main()
{
    Complex c1(10, 5), c2(2, 2), c3;
//  c3 = c1.operator+(c2);                             Statement 1
    c3 = c1 + c2;                                   // Statement 2
    cout << c3.real << " " << c3.imag << endl;      => 12+i7
}
```

`Statement 1` and `Statement 2` will perform the same operation.

## Operator Overloading using friend function

```cpp
class Complex
{
private:
    int real;
    int imag;

public:
    Complex(int real = 0, int imag = 0)
    {
        this->real = real;
        this->imag = imag;
    }

    void display()
    {
        cout << real << " + i" << imag << endl;
    }

    friend Complex operator+(Complex c1, Complex c2);
};

Complex operator+(Complex c1, Complex c2)
{
    Complex temp;
    temp.real = c1.real + c2.real;
    temp.imag = c1.imag + c2.imag;
    return temp;
}

void main()
{
    Complex c1(10, 5), c2(2, 2), c3;
    // c3 = operator+(c1,c2);
    c3 = c1 + c2;
    c3.display();                               => 12 + i7
}
```

`friend` function has to be declared inside the class and defined outside the class.

## Overloading Insertion Operator

First let's see a basic display function

```cpp
class Complex
{
private:
    int real;
    int imag;

public:
    Complex(int real = 0, int imag = 0)
    {
        this->real = real;
        this->imag = imag;
    }

    void display()
    {
        cout << real << " + i" << imag << endl;
    }
};

void main()
{
    Complex c1(10, 5);
    c1.display();
}
```

Now let us see Inseration Operator Overloading

```cpp
class Complex
{
private:
    int real;
    int imag;

public:
    Complex(int real = 0, int imag = 0)
    {
        this->real = real;
        this->imag = imag;
    }

    friend ostream &operator<<(ostream &, Complex c);
};

ostream &operator<<(ostream &out, Complex c)
{
    out << c.real << " + i" << c.imag;
    return out;
}

void main()
{
    Complex c1(10, 5);
    cout << c1;
}
```

We can observe that fucntion operator<<() function is getting two parameters of different classes (ostream class and Complex class).

So we has to make it as a friend function.

# Inheritance

```cpp
class Rectangle
{
private:
    int length;
    int breadth;

public:
    Rectangle();
    Rectangle(int l, int b);
    Rectangle(Rectangle &r);
    int getLength() { return length; }
    int getBreadth() { return breadth; }
    void setLength(int l);
    void setBreadth(int b);
    int area();
    int perimeter();
    bool isSquare();
    ~Rectangle();
};

class Cuboid : public Rectangle
{
private:
    int height;

public:
    Cuboid(int l = 0, int b = 0, int h = 0)
    {
        setLength(l);
        setBreadth(b);
        height = h;
    }

    int getHeight()
    {
        return height;
    }

    void setHeight(int h)
    {
        height = h;
    }

    int Volume()
    {
        return getLength() * getBreadth() * height;
    }
};

void main()
{
    Cuboid c1(10, 7, 5);
    cout << c1.Volume() << endl;
}
```

## Constructors in Inheritance

Constructor of base class is executed first then the constructor of derived class is executed.

By default, non-parameterised constructor of base class is executed.

**Program 1**

```cpp
class Base
{
public:
    Base(){cout<<"Non-param Base"<<endl;}
    Base(int x){cout<<"Param of Base "<<x<<endl;}
};

class Derived:public Base
{
public:
    Derived(){cout<<"Non-Param Derived"<<endl;}
    Derived(int y){cout<<"Param of Derived "<<y<<endl;}
};

int main()
{
    Derived d;
}
```

Output

```
Non-param Base
Non-param Derived
```

**Program 2**

```cpp
class Base
{
public:
    Base(){cout<<"Non-param Base"<<endl;}
    Base(int x){cout<<"Param of Base "<<x<<endl;}
};

class Derived:public Base
{
public:
    Derived(){cout<<"Non-Param Derived"<<endl;}
    Derived(int y){cout<<"Param of Derived "<<y<<endl;}
};

int main()
{
    Derived d(10);
}
```

Output

```
Non-param Base
Param of Derived 10
```

---

Parameterised constructor of base class must be explicitly called from derived class constructor.

```cpp
class Base
{
public:
    Base(){cout<<"Non-param Base"<<endl;}
    Base(int x){cout<<"Param of Base "<<x<<endl;}
};

class Derived:public Base
{
public:
    Derived(){cout<<"Non-Param Derived"<<endl;}
    Derived(int y){cout<<"Param of Derived "<<y<<endl;}

    Derived(int x,int y):Base(x)    // calling base class constructor explicitly
    {
        cout<<"Param of Derived "<<y<<endl;
    }
};

int main()
{
    Derived d(5,10);
}
```

Output

```
Param of Base 5
Param of Derived 10
```

## Generalization and Specialization

**Purpose of Inheritance:**

Generalization

- It is bottom up approach.
- Derived classes already exists, but to simplify things we make a generalized Base class.
- We can use a generalized(same) name for different classes : polymorphic
- For example, Car - Innova, Swift, Fortuner
  - We only need to learn How to Drive a car, then we can ride any car we want (Innova, Swift, Fortuner)
- Purpose of Generalization is to achieve `Polymorphism`

Specialization

- It is top down approach.
- Derived classes are inherited from already existing base class (More specilized version of base class is made)
- It shares it features to its child classes
- For example, Rectangle - Cuboid
  - Cuboid inherits the features of Rectangle.
- Purpose of Specialization is to achieve `Inheritance`

## Base Class Pointer and Derived Class Object

Consider these classes

```cpp
class BasicCar
{
public:
    void start()
    {
        cout << "Car started" << endl;
    }
};

class AdvanceCar : public BasicCar
{
public:
    void playMusic()
    {
        cout << "Music Playing" << endl;
    }
};
```

**Branch 1**

```cpp
void main()
{
    BasicCar *bc;
    bc = new AdvanceCar();
    bc->start();
//  bc->playMusic();            This will generate error
}
```

Once the BasicCar pointer is assigned AdvanceCar object

- then the Pointer will treat the object as if it is a BasicCar object.

Hence we **cannot** access the AdvanceCar methods.

> Note : Data members are accessed according to the type of pointer we have. and NOT according to the object we have got.
>
> Base Class Pointer can Hold the object of Derived class, But It can only call those methods which are defined in the Base class.

**Branch 2**

```cpp
void main()
{
    AdvanceCar *ac;
    ac = new BasicCar();
}
```

This branch is erroneous.

We can never assign BasicCar object to AdvanceCar pointer.

- Becuase the AdvanceCar pointer is supposed to have playMusic() functionality as well,

- But we won't get that functionality, because we're trying to assign BasicCar object.

# Polymorphism

## Function Overriding

Redefining a function of base class in derived class is known as function overriding.

Function overriding is used for achieving runtime polymorphism.

Prototype of a overriding function must be exactly same as base class function.

```cpp
class Base
{
public:
    void fun()
    {
    cout<<"fun of Base"<<endl;
    }
};

class Derived: public Base
{
public:
    void fun()
    {
    cout<<"fun of Derived"<<endl;
    }
};

int main()
{
    Base *b = new Base();
    b->fun();                       => fun of Base

    Derived *d = new Derived();
    d->fun( );                      => fun of Derived

    // Base class pointer assumes that it is pointing to the base class object, so It will only access the base class methods.
    Base *b = new Derived();
    b->fun();                       => fun of Base
    // This didn't called Drived Class Method, It happened because the Base class function is not declared virtual.
}
```

## Virtual Functions

```cpp
class BasicCar
{
public:
    virtual void start(){cout<<"BasicCar started"<<endl;}       // Virtual function
};

class AdvanceCar: public BasicCar
{
public:
    void start(){cout<<"AdvanceCar Started"<<endl;}
};

void main()
{
    BasicCar *p = new AdvanceCar();
    p->start();                             => AdvanceCar Started
}
```

**When** a Base class function is declared virtual and it is overridden in derived class,

- then the function call will not be based on the pointer, it will be based on the Object.

- Here, the AdvanceCar start() will be called because
  - The base class function is overridden by derived class
  - The base class function is declared virtual.

## Runtime Polymorphism

Runtime Polymorphism is achieved using function overriding.

```cpp
class BasicCar
{
public:
    virtual void start(){cout<<"BasicCar Started"<<endl;}       // Virtual function
};

class AdvanceCar: public BasicCar
{
public:
    void start(){cout<<"AdvanceCar Started"<<endl;}
};

void main()
{
    BasicCar *p = new AdvanceCar();
    p->start();                             => AdvanceCar Started

    p = new BaseCar();
    p->start();                             => BasicCar Started
}
```

The binding of `start()` happens at runtime, becuase it has to know that what object will be given to the pointer.

And the allocation of the object happens at runtime.

So, which function `p->start()` has to call will be resolved at runtime.

---

Summary: class car is defined, then sub classes override, then base class method made as pure virtual function

```cpp
class Car
{
public:
    virtual void start()=0;                 // Pure virtual function
};

class Innova:public Car
{
public:
    void start(){cout<<"Innova Started"<<endl;}
};

class Swift:public Car
{
public:
    void start(){cout<<"Swift Started"<<endl;}
};

int main()
{
    Car *p = new Innova();
    p->start();                             => Innova Started
    p = new Swift();
    p->start();                             => Swift Started
}
```

Here we have `generalized` the two classes (Innova and Swift) to class Car.

Now, we are able to use start() in main() function dynamically (Run time binding of functions).

Polymorphism : Same name different function

> Derived class must override virtual functions.
>
> Pure virtual functions forces the child classes to override that pure virtual function.

> Note : A pure virtual function (or abstract function) is a virtual function for which we don’t have an implementation, we only declare it. A pure virtual function is declared by assigning 0 in the declaration.

## Abstract class

If a class is having a pure virtual function then it is called Abstract class.

Abstract class can have concrete functions also.

We cannot create a object of abstract class.

But Pointer of abstract class can be created.

Pointer of abstract class can hold object of derived class.

Derived class can must override pure virtual function, otherwise it will also become a abstract
class.

```cpp
class Base                              // Abstract class
{
public:
    virtual void fun1()=0;              // Pure virtual function
    virtual void fun2()=0;              // Pure virtual function
    void fun3()                         // Concrete function
    {
        cout<<"fun 3 of Base"<<endl;
    }
};

class Derived :public Base
{
public:
    void fun1()
    {
        cout<<"fun1 of Derived"<<endl;
    }
    void fun2()
    {
        cout<<"fun2 of Derived"<<endl;
    }
};
int main()
{
    Derived d;
    d.fun1();
    d.fun2();
}
```

```cpp
class Base                                  // Interface
{
public:
    virtual void fun1()=0;                  // Pure virtual function
    virtual void fun2()=0;                  // Pure virtual function
};

class Derived :public Base
{
public:
    void fun1()
    {
        cout<<"fun1 of Derived"<<endl;
    }
    void fun2()
    {
        cout<<"fun2 of Derived"<<endl;
    }
};
int main()
{
    Derived d;
    d.fun1();
    d.fun2();
}
```

## Types of Base classes

- Base class with All Concrete Functions

  - Purpose of this base class is to achieve **Resuability** (That is, Inheritance).

- Base class with Some concrete functions and Some Pure Virtual Functions

  - Purpose of this base class is to achieve **Resuability** and **Polymorphism**.
  - It is also called **Abstract class**

- Base class with All Pure Virtual Functions
  - Purpose of this base class is to achieve **Polymorphism**.
  - It is also called **Abstract class**
  - It is also called **Interface**

# Friend and Static Members

## Friend

### Friend Function

They are the non-member functions that can access and manipulate the private and protected members of the class for they are declared as friends.

They can access member of a class upon their objects

A friend function can be:

- global function
- member function of another class

```cpp
class Test
{
    private:
        int a;
    protected:
        int b;
    public:
        int c;

        friend void fun();
};

void fun()
{
    Test t1;
    t1.a = 10;
    t1.b = 20;
    t1.c = 30;
    // a = 15;      Directly trying to access data member will generate error
}
```

we can access private and protected members of the class using a object inside the friend function

### Friend Class

A friend class can access private and protected members of other classes in which it is declared as a friend.

All the functions of friend class can access private and protected members of other class

```cpp
class Two;

class One
{
    private:
        int a;
    protected:
        int b;
    public:
        int c;
        friend Two;
};

class Two
{
    public:
        One o1;
        void fun()
        {
            o1.a = 1;
            o1.b = 2;
            o1.c = 3;
        }
}
```

## Static

### Static Data Member

Static data members are members of a class.

Only one instance of static members is created and shared by all objects.

They can also be accessed directly using class name.

### Static Member Function

Static members functions are functions of a class, they can be called using class name, without
creating object of a class.

They can access only static data members of a class, they cannot access non-static members
of a class.

### Example

```cpp
class Test
{
private:
    int a;
    static int count;
public:
    Test()
    {
        a=10;
        count++;
    }
    static int getCount()
    {
        return count;
    }

};

int Test::count=0;

int main()
{
    Test t1,t2;
    cout<<t1.getCount()<<endl;
    // t1.count=10;                 This can also be done, if the static data member is public
    cout<<Test::getCount()<<endl;
}
```

**Uses**

- Static members can be used as a counter
- They can be used as a shared memory for all the objects
- They can Provide about a class

## Nested class

Firstly, the Nested class works exactly the same as any other class, declared outside of the outer class.

Inner class can access the static members of outer class.

Object of Inner class can be created inside the outer class.

Outer class can access all the public member is Inner class(using its object).

```cpp
class Outer
{
    public:
        void fun()
        {
            i.display();            // Using members of Inner class
        }

        class Inner
        {
            public:
                void display()
                {
                    cout<< "Display of Inner"<<endl;
                }
        };
        Inner i;                    // Creating object of Inner class
};

void main()
{
    Outer o1;                                       // Creating object of Outer class
    o1.fun();               => Display of Inner
    Outer::Inner i1;                                // Creating object of Inner class
    i1.display();           => Display of Inner
}
```

# Exception Handling

```cpp
#include <iostream>
using namespace std;

int division(int x, int y)
{
    if (y == 0)
        throw 1;
    return x / y;
}

int main()
{
    int a = 10, b = 2, c;
    try
    {
        c = division(a, b);
        cout << c << endl;
    }
    catch (int err)
    {
        cout << "Division failed: " << err << endl;
    }
    catch (...)
    {
        cout << "Catch all exceptions" << endl;
    }
    return 0;
}
```

# Template Classes

They can work for any type of data

**Program 1 : `int` specific class for stack**

```cpp
class Stack
{
private:
    int *stk;
    int top;
    int size;

public:
    Stack(int sz)
    {
        size = sz;
        top = -1;
        stk = new int[size];
    }
    void push(int x);
    int pop();
};
void Stack::push(int x)
{
    if (top == size - 1)
        cout << "Stack is Full";
    else
    {
        top++;
        stk[top] = x;
    }
}
int Stack::pop()
{
    int x = 0;
    if (top == -1)
        cout << "Stack is Empty" << endl;
    else
    {
        x = stk[top];
        top--;
    }
    return x;
}
void main()
{
    Stack s(10);
    s.push(10);
    s.push(23);
    s.push(33);
}
```

**Program 2 : generic class for stack**

```cpp
template <class T>
class Stack
{
private:
    T *stk;
    int top;
    int size;

public:
    Stack(int sz)
    {
        size = sz;
        top = -1;
        stk = new T[size];
    }
    void push(T x);
    T pop();
};

template <class T>
void Stack<T>::push(T x)
{
    if (top == size - 1)
        cout << "Stack is Full";
    else
    {
        top++;
        stk[top] = x;
    }
}

template <class T>
T Stack<T>::pop()
{
    T x = 0;
    if (top == -1)
        cout << "Stack is Empty" << endl;
    else
    {
        x = stk[top];
        top--;
    }
    return x;
}

void main()
{
    Stack<int> s(10);
    s.push(10);
    s.push(23);
    s.push(33);
}
```

# Constants Preprocessors and Namespaces

## Constants

syntax:

`const int a = 10;`

or

`int const a = 10;`

### Constant Identifiers

We cannot point to a constant identifier , using variable pointer.

```cpp
    const int x = 10;
    int *ptr = &x;          // Invalid Statement
```

But this is possible,

```cpp
    const int x = 10;
    const int *ptr = &x;          // Valid Statement
```

### Pointer to Constant (Data is Constant)

In the pointers to constant, the data pointed by the pointer is constant and cannot be changed. Although, the pointer itself can change and points somewhere else (as the pointer itself is a variable).

#### Base Operation

```cpp
    int x = 10;
    int *ptr = &x;
    ++(*ptr);       // Valid statement
```

#### Operation on constant type pointer

```cpp
    int x = 10;
    const int *ptr = &x;
    ++(*ptr);       // Invalid statement (we cannot modify the data value of the pointer to constant)
```

Here, `ptr` is a pointer to integer constant, so the ptr will treat x as a constant.

Pointer assumes that it is pointing to a constant type variable.

It can also be written as `int const *ptr = &x;`

#### Assigning another constant to the pointer

```cpp
    int x = 10;
    const int *ptr = &x;
    ++(*ptr);       // Invalid statement

    int y = 20;
    ptr = &y;       // Valid statement
    ++(*ptr);       // Invalid statement
```

Here, the pointer is NOT constant (It is a variable) , but the value pointed by pointer is constant.

### Constant Pointer (Pointer is constant)

In constant pointers, the pointer points to a fixed memory location, and the value at that location can be changed because it is a variable, but the pointer will always point to the same location because it is made constant here.

```cpp
    int x = 10;
    int * (const ptr) = &x;
    ++(*ptr);       // Valid statement

    int y = 20;
    ptr = &y;       // Invalid statement
```

### Constant Pointer to Constant

The data pointed to by the pointer is constant, so cannot be changed and The pointer itself is constant, so it cannot change or point somewhere else.

```cpp
    int x = 10;
    const int * const ptr = &x;
    ++(*ptr);       // Invalid statement

    int y = 20;
    ptr = &y;       // Invalid statement
    ++(*ptr);       // Invalid statement
```

### Constant Methods

If a Member function of a class is not allowed to change the data members of class, then we can use `const` keyword after the fucntion name.

```cpp
class Demo
{
    public:
        int x = 10;
        int y = 20;

        void Display() const
        {
            x++;                // Now, this statement will give error
            cout<< x << " " << y << endl;
        }
}
```

### Constant Formal Parameters

```cpp
void fun(const int &x, const int &y)
{
    x++;                            // This statement will give error
    cout<< x << " " << y << endl;
}

void main()
{
    int a = 10, b = 20;
    fun(a,b);
}
```

When we use call by reference, the actual variables are used in the function.

Those variables can also be altered in the fucntion.

To avoid this problem, we can declare the formal parameters as `const`, so that the parameters will stay constant during the execution of function and its value will not be changed.

## Preprocessor Directives (Macros)

They are instructions to compiler.

They are processed before compilation.

The replacement is performed before the compilatioon.

They are used for defining symbolic constant.

They are used for defining functions.

They also support conditional definition.

---

```cpp
#define PI 3.14

void main()
{
    cout<<PI;           => 3.14
}
```

---

```cpp
#define PI 3.14
#define PI 3

void main()
{
    cout<<PI;           => 3
}
```

---

`ifndef` is conditional directive, which means "If not defined"

```cpp
#define PI 3.14

#ifndef PI
    #define PI 3
#endif

void main()
{
    cout<<PI;           => 3.14
}
```

Here , if value of PI is not defined already, then It will get executed.
But since we already have defined PI, so It won't get executed.

---

```cpp
#ifndef PI
    #define PI 3
#endif

void main()
{
    cout<<PI;           => 3
}
```

Since we haven't already defined the value of PI, so it will get executed.

---

```cpp
#define maxi(a,b) (a > b ? a : b)

void main()
{
    cout<< maxi(10,12);         => 12
}
```

---

```cpp
#define msg(x) #x

void main()
{
    cout<< msg(Hello);          => Hello
}
```

`#` before `x` makes the value of `x` as string (It wraps the value of x in double quotes).

Here, it changes it into `"Hello"`

## Namespaces

They are used for removing name conflict between functions, classes and objects.

### Base Problem

```cpp
void fun()
{
    cout<< "First" <<endl;
}

void fun()
{
    cout<< "Second" <<endl;
}

void main()
{
    fun();
}
```

This program will give error that , redeclaration of funtion `fun()` is done.

### Using Namespaces

```cpp
namespace first
{
    void fun()
    {
        cout<< "First" <<endl;
    }
};

namespace second
{
    void fun()
    {
        cout<< "Second" <<endl;
    }
};

void main()
{
    fun();              // Statement 1 : Invalid Statement
    first::fun();       => First
    second::fun();      => Second
}
```

`statement 1` will give error because function `fun()` is not openly declared.

---

```cpp
namespace first
{
    void fun()
    {
        cout<< "First" <<endl;
    }
};

namespace second
{
    void fun()
    {
        cout<< "Second" <<endl;
    }
};

using namespace first;
void main()
{
    fun();              => First        // Valid Statement
    second::fun();      => Second
}
```

# Destructors

Constructors are used for acquiring the resources.

Destructors are used for releasing the resources acquired by object of the class.

```cpp
class Demo
{
    public:
        Demo()
        {
            cout<< "Constructor is Called" << endl;
        }
        ~Demo()
        {
            cout<< "Destructor is Called" << endl;
        }
};

void main()
{
    Demo d;
}
```

**Output**

```
Constructor is Called
Destructor is Called
```

Constructor is called when the object is created.

Destructor is called when the object goes out of scope.

## Destructors with Dynamic Objects

```cpp
class Demo
{
    public:
        Demo()
        {
            cout<< "Constructor is Called" << endl;
        }
        ~Demo()
        {
            cout<< "Destructor is Called" << endl;
        }
};

void main()
{
    Demo *d = new Demo();
}
```

**Output**

```
Constructor is Called
```

When we create object dynamically using `new` operator, only the constructor is called.

We need to delete the object explicitly using `delete` operator, and it will call the destructor.

```cpp
class Demo
{
    public:
        Demo()
        {
            cout<< "Constructor is Called" << endl;
        }
        ~Demo()
        {
            cout<< "Destructor is Called" << endl;
        }
};

void main()
{
    Demo *d = new Demo();
    delete d;
}
```

**Output**

```
Constructor is Called
Destructor is Called
```

## Use of Destructors

```cpp
class Demo
{
    int *ptr;
    public:
        Demo()
        {
            ptr = new int[10];
            cout<< "Constructor is Called" << endl;
        }
        ~Demo()
        {
            delete []ptr;
            cout<< "Destructor is Called" << endl;
        }
};

void main()
{
    Demo *d = new Demo();
    delete d;
}
```

**Output**

```
Constructor is Called
Destructor is Called
```

When object is deleted, the memory(resources) acquired by it should also be deleted.

So we can include those operators in the destructor.

## Destructors in Inheritance

```cpp
class Base
{
    public:
        Base()
        {
            cout << "Constructor Base" << endl;
        }
        ~Base()
        {
            cout << "Destructor Base" << endl;
        }
};

class Derived : public Base
{
    public:
        Derived()
        {
            cout << "Constructor Derived" << endl;
        }
        ~Derived()
        {
            cout << "Destructor Derived" << endl;
        }
};

void main()
{
    Derived d;
}
```

**output**

```
Constructor Base
Constructor Derived

Destructor Derived
Destructor Base
```

### Destructor for dynamic objects

```cpp
class Base
{
    public:
        Base()
        {
            cout << "Constructor Base" << endl;
        }
        ~Base()
        {
            cout << "Destructor Base" << endl;
        }
};

class Derived : public Base
{
    public:
        Derived()
        {
            cout << "Constructor Derived" << endl;
        }
        ~Derived()
        {
            cout << "Destructor Derived" << endl;
        }
};

void main()
{
    Base *ptr = new Derived();
    // Some processing
    delete ptr;
}
```

**output**

```
Constructor Base
Constructor Derived

Destructor Base
```

It does not call the destructor of derived class, since pointer assumes that it holds a Base class object.

### Virtual Destructor

```cpp
class Base
{
    public:
        Base()
        {
            cout << "Constructor Base" << endl;
        }
        virtual ~Base()
        {
            cout << "Destructor Base" << endl;
        }
};

class Derived : public Base
{
    public:
        Derived()
        {
            cout << "Constructor Derived" << endl;
        }
        ~Derived()
        {
            cout << "Destructor Derived" << endl;
        }
};

void main()
{
    Base *ptr = new Derived();
    // Some processing
    delete ptr;
}
```

**output**

```
Constructor Base
Constructor Derived

Destructor Derived
Destructor Base
```

# IOstream

Stream is flow of data.

They are used for accessing data from outside the program.

I/O Streams are used for input and output data to and from the program.

C++ provides class for accessing input output operations.

Iostream is a base class for all classes.

Istream is for input.

- Cin is the object of istream.

Ostream is for output.

- Cout is an object of ostream.

## Writing in a file

```cpp
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ofstream file("myfile.txt", ios::trunc);

    file << "John" << endl;
    file << 21 << endl;
    file << CSE << endl;

    file.close();
}
```

## Reading from a file

```cpp
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream file("myfile.txt");

    if(file.is_open())
        cout << "File is Opened" << endl;

    string name;
    int roll;
    string branch;

    file >> name >> roll >> branch;

    if(file.eof())
        cout << "End of file reached" <<endl;

    file.close();

    cout << "Name: " << name << endl;
    cout << "Roll NO: " << roll << endl;
    cout << "Branch: " << branch << endl;
}
```

## Serialization

Serialization is a process of string and retrieving state of an object.

```cpp
class Student
{
private:
    string name;
    int roll;
    string branch;
public:
    Student(){}
    Student(string n,int r,string b)
    {
        name=n;
        roll=r;
        branch=b;
    }
    friend ofstream & operator<<(ofstream &ofs,Student s);
    friend ifstream & operator>>(ifstream &ifs,Student &s);
    friend ostream & operator<<(ostream &os,Student &s);
};

ofstream & operator<<(ofstream &ofs,Student s)
{
 ofs<<s.name<<endl;
 ofs<<s.roll<<endl;
 ofs<<s.branch<<endl;
 return ofs;
}

ifstream & operator>>(ifstream &ifs,Student &s)
{
 ifs>>s.name;
 ifs>>s.roll;
 ifs>>s.branch;
 return ifs;
}

ostream & operator<<(ostream &os,Student &s)
{
 os<<"Name "<<s.name<<endl;
 os<<"Roll "<<s.roll<<endl;
 os<<"Branch "<<s.branch<<endl;
 return os;
}

int main()
{
    ofstream ofs("Test.txt");
    Student s1("John",10,"CS");

    ofs<<s1;
    ofs.close();

    Student s2;
    ifstream ifs("Test.txt");
    ifs>>s2;

    cout<<s2;
}
```

# Standard Template Library

It contains

Algorithms

Containers

Iterators

# Cpp11

## Type Inference

It refers to automatic deduction of the data type of an expression in a programming language.

As all the types are deduced in the compiler phase only, the time for compilation increases slightly but it does not affect the run time of the program.

### auto Keyword

The auto keyword specifies that the type of the variable that is being declared will be automatically deducted from its initializer.

In the case of functions, if their return type is auto then that will be evaluated by return type expression at runtime.

Good use of auto is to avoid long initializations when creating iterators for containers.

> Note : The variable declared with auto keyword should be initialized at the time of its declaration only or else there will be a compile-time error.

> Note : `auto` becomes int type if even an integer reference is assigned to it. To make it reference type, we use auto &.

```cpp
int& fun() {};          // Function that returns a ‘reference to int’ type

void main()
{
    auto m = fun();     // m will default to int type instead of int& type
    auto& n = fun();    // n will be of int& type because of use of extra & with auto keyword
}
```

### decltype Keyword

`auto` lets you declare a variable with a particular type whereas `decltype` lets you extract the type from the variable.

```cpp
int main()
{
    int x = 5;

    // j will be of type int : data type of x
    decltype(x) j = x + 5;

    cout << typeid(j).name();                   => i
}
```

## final Keyword

It restricts Inheritance.

We cannot derive from a base class which is declared final.

```cpp
class Base final
{

};

class Derived : public Base     // This will generate error
{

};
```

---

It is also used to restrict function overriding.

```cpp
class Base
{
    virtual void show() final       // Function needs to be virtual
    {

    }
};

class Derived : public Base
{
    void show()             // This will generate error
    {

    }
};
```

Final functions of parent class cannot be overridden in child class.

## Lambda Expressions

They are inline functions which can be used for short snippets of code that are not going to be reused and therefore do not require a name.

syntax:

```
[ captured variables ] (parameters) -> return-type
{
   definition of method
}
```

---

**Example**

```cpp
void main()
{
    [] () {cout<<"Hello"<<endl;} ();       => Hello
}
```

The function will also be called.

---

**Sending Parameters**

```cpp
void main()
{
    [] (int a, int b) {cout<<"Sum is "<< a + b <<endl;} (10, 20);       => 30
}
```

---

**Returning Value**

```cpp
void main()
{
    cout<<( [] (int a, int b) {return a+b;} (10, 20) );                 => 30
}
```

---

**Assigning the returning value to a variable**

```cpp
void main()
{
    int sum = [] (int a, int b) {return a+b;} (10, 20);
    cout<<sum;                                                          => 30
}
```

```cpp
void main()
{
    int sum = [] (int a, int b) -> int {return a+b;} (10, 20);
    cout<<sum;                                                          => 30
}
```

---

**Assigning the function to a reference (pointer)**

```cpp
void main()
{
    auto f = [] () {cout << "Hello World" << endl;};
    f();                                                                => Hello World
}
```

Function call is made at `f();`

---

**Accessing local variables of a function inside the lambda expression**
(captured variables)

```cpp
void main()
{
    int a = 10;

    auto f = [a] () {cout << a << endl;};       // statement 1

    f();                                        => 10
    a++;
    f();                                        => 10
}
```

The value of `a` is replaced at the definition of the lambda expression, hence it does not access the latest/updated value of `a`.

Moreover, **Here** we cannot modify the value of captured variables inside the lambda expression.

That is, we cannot perform `a++` inside the lambda expression.

---

To solve these issues, we can use references.

```cpp
void main()
{
    int a = 10;

    auto f = [&a] () {cout << a++ << endl;};

    f();                                        => 10
    a++;
    f();                                        => 12
}
```

---

**Sending Lambda Expression to function as parameter**

```cpp
template <typename T>
void fun(T p)
{
    p();
}

void main()
{
    int a = 10;

    auto f = [&a] () {cout << a++ << endl;};

    fun(f);                                         => 10
    fun(f);                                         => 11
}
```

## Smart Pointers

They automatically deallocates the heap memory, when objects goes out of scope.

### Base Problem

```cpp
void fun()
{
    Rectangle *p = new Rectangle();
    // pass
}

void main()
{
    fun();
}
```

When function `fun()` is finished executing,

- The pointer is deleted from the activation record of the function.
- But the value allocated in the heap memeory is not released.
- That is, It does not deallocate the object, when it goes out of scope.

In this way, there is wastage of memory.

To solve this problem, we need to delete the memory explicitly using `delete` keyword.

```cpp
void fun()
{
    Rectangle *p = new Rectangle();
    // pass
    delete p;
}

void main()
{
    fun();
}
```

This solves the problem.

### Usage of smart pointer

```cpp
void fun()
{
    unique_ptr<Rectangle> p(new Rectangle());
    cout<< p->area() <<endl;
    cout<< p->perimeter() <<endl;
}

void main()
{
    fun();
}
```

The `unique_ptr` class deletes the pointer as well as deallocates the memory, when the pointer goes out of scope.

So, we don't have to worry about deallocating the heap memory.

### Types of Smart Pointes

#### unique_ptr

Upon a object, only one pointer will be pointing, at a time.

```cpp
class Rectangle
{
private:
    int length;
    int breadth;

public:
    Rectangle(int l=1, int b=1)
    {
        length=l;
        breadth=b;
    }
    int area()
    {
        return length*breadth;
    }
    int perimeter()
    {
        return 2*(length+breadth);
    }
    ~Rectangle();
};

void main()
{
    unique_ptr<Rectangle> ptr1(new Rectangle(10, 5));
    cout << ptr1 -> area();                             => 50

    unique_ptr<Rectangle> ptr2 = ptr1;                  // Invalid
    unique_ptr<Rectangle> ptr2(ptr1);                   // Invalid

    unique_ptr<Rectangle> ptr2;
    ptr2 = move(ptr1);
    cout << ptr2 => area();                             => 50

    cout << ptr1 -> area();                             // Error
}
```

#### shared_ptr

More than one pointer can point to the same object.

It keeps record of number of pointers pointing to the same object.

```cpp
class Rectangle
{
private:
    int length;
    int breadth;

public:
    Rectangle(int l=1, int b=1)
    {
        length=l;
        breadth=b;
    }
    int area()
    {
        return length*breadth;
    }
    int perimeter()
    {
        return 2*(length+breadth);
    }
    ~Rectangle();
};

void main()
{
    shared_ptr<Rectangle> ptr1(new Rectangle(10, 5));
    cout << ptr1 -> area();                             => 50

    shared_ptr<Rectangle> ptr2 = ptr1;                  // Valid
    shared_ptr<Rectangle> ptr2(ptr1);                   // Valid

    cout << ptr2 => area();                             => 50

    cout << ptr1 -> area();                             => 50

    cout << ptr1.use_count();                           => 2
}
```

#### weak_ptr

- It is almost same as `shared_ptr`.
- More than one pointer can point to the same object.
- It doesn't keep record of number of pointers pointing to the same object.
- They have weak hold over the object.
- They are useful to avoid deadlock.

## Inclass Initializer and Delegation of Constructors

```cpp
class Test
{
    int x = 10;
    int y = 20;

public:
    Test(int a, int b)
    {
        x = a;
        y = b;
    }

    Test() : Test(1,1)
    {}
}
```

Inclass Initializer : We can initialize the data members inside the class itself.

> Note : Earlier, we could not initialize the data members of the class.

Delegation of Constructors : One contructor can call another constructor within the same class.

## Ellipsis

They are Used for defining variable argument functions.

… is used as symbol of ellipsis.

Printf and scanf of C language are example of ellipsis.

```cpp
int sum(int n,...)
{
    va_list list;
    va_start(list,n);

    int x;
    int s=0;
    for(int i=0;i<n;i++)
    {
        x = va_arg(list,int);
        s += x;
    }
    return s;
}
int main()
{
    cout << sum(3,10,20,30) << endl;
    cout << sum(5,1,2,3,4,5) << endl;
}
```
