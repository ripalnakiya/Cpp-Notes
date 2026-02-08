# Abstract
<show-structure depth="2"/>

## Abstract Function

A **pure virtual function** is a virtual function
that has no implementation in the base class and is declared using `= 0`.

Pure virtual function forces the derived classes to override it.

```c++
class Car
{
public:
    virtual void start() = 0; // Pure virtual function
};

class Mercedes : public Car
{
public:
    void start() { cout << "Mercedes" << endl; }
};

class Audi : public Car
{
public:
    void start() { cout << "Audi" << endl; }
};

int main()
{
    Car* p = new Mercedes();
    p->start();         // "Mercedes"
    p = new Audi();
    p->start();         // "Audi"
}
```

Here we have **generalized** the two classes (Mercedes and Audi) to class Car.

Now, we are able to use `start()` function dynamically (**run time binding** of functions).

We can use the `override` keyword to
explicitly state that a member function is intended
to override a virtual function from a base class,
allowing the compiler to verify this.

```c++
class Car
{
public:
    virtual void start() = 0; // Pure virtual function
};

class Mercedes : public Car
{
public:
    void start() override { cout << "Mercedes" << endl; }
};

class Audi : public Car
{
public:
    void start() override { cout << "Audi" << endl; }
};
```

## Abstract Class

It is a class that has atleast **one pure virtual function**.
It can also have concrete functions.

- We **cannot create a object** of abstract class.
- But pointer of abstract class can be created.
- Pointer of abstract class can hold object of derived class.

A derived class needs to **override pure virtual functions** of base class, 
otherwise it will also become a abstract class.

```c++
class Base
{
public:
    virtual void read() = 0;    // Pure virtual function
    virtual void write() = 0;   // Pure virtual function
    void speak()                // Concrete function
    {
        cout << "Base Speak()" << endl;
    }
};

class Derived : public Base
{
public:
    void read() override
    {
        cout << "Derived read()" << endl;
    }

    void write() override
    {
        cout << "Derived write()" << endl;
    }
};

int main()
{
    Derived d;
    d.read();   // Derived read()
    d.write();  // Derived write()
    d.speak();  // Base speak()
}
```

## Interface

An interface in C++ is an abstract class 
that defines a contract using **only pure virtual functions**, 
leaving all implementation details to derived classes.

```c++
class Base
{
public:
    virtual void read() = 0;     // Pure Virtual function
    virtual void write() = 0;    // Pure Virtual function
    virtual void speak() = 0;    // Pure Virtual function
};

class Derived : public Base
{
public:
    void read() override
    {
        cout << "Derived read()" << endl;
    }

    void write() override
    {
        cout << "Derived write()" << endl;
    }

    void speak() override
    {
        cout << "Derived speak()" << endl;
    }
};

int main()
{
    Derived d;
    d.read();   // Derived read()
    d.write();  // Derived write()
    d.speak();  // Derived speak()
}
```

## Types of Base classes

| Base Class with ...                         | Abstract Class ? | Main Purpose                             | Common Name               |
|---------------------------------------------|------------------|------------------------------------------|---------------------------|
| All concrete functions                      | ❌ No             | Code reuse via inheritance               | Concrete base class       |
| Some concrete + some pure virtual functions | ✅ Yes            | Code reuse **and** runtime polymorphism  | Abstract class            |
| All pure virtual functions                  | ✅ Yes            | Runtime polymorphism, defining contracts | Interface (by convention) |
