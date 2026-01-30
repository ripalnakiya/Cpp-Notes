# Table of Contents

[1. IOstream](#iostream)

[2. cpp11](#cpp11)

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
