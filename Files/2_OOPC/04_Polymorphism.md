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

- then the function call will not be based on the pointer , it will be based on the Object.

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
    virtual void fun1()=0;                  // Pure Virtual function
    virtual void fun2()=0;                  // Pure Virtual function
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
