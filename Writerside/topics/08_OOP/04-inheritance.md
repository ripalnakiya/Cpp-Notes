# Inheritance
<show-structure depth="2"/>

It is the capability of a class to derive properties of another class.

![Inheritance](inheritance.png){ height=450 }

Single Inheritance

```c++
class DerivedName : visibilityMode BaseClass {
    
};
```

Multiple Inheritance
```c++
class DerivedName : visibilityMode1 BaseClass1, visibilityMode2 BaseClass2 {
    
};
```

## Visibility Mode

It controls the "access specifier to be" 
for the inheritable members of base class in the derived class.

| Inheritance Mode | Base `public` → Derived | Base `protected` → Derived | Base `private` → Derived |
|------------------|-------------------------|----------------------------|--------------------------|
| `public`         | `public`                | `protected`                | ❌ not accessible         | 
| `protected`      | `protected`             | `protected`                | ❌ not accessible         |
| `private`        | `private`               | `private`                  | ❌ not accessible         |

If the inherited members become `private` in derived class, 
they cannot be inherited further if the derived class happens
to be a base class of another class.

If we specify nothing, the class will inherit privately.

## Access Control

A derived class **inherits all** data members and member functions 
of the base class as part of its object layout.

This includes private, protected, and public members, 
and therefore the size of a derived class object includes 
all base class members, including private ones.

However, the derived class has direct access 
only to the public and protected members of the base class.

Private members of the base class, although present in the derived object, 
are accessible only to the base class itself.

## Inheritance Example

```c++
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
    Cuboid(int l = 0, int b = 0, int h = 0) {
        setLength(l);
        setBreadth(b);
        height = h;
    }

    int getHeight() {
        return height;
    }

    void setHeight(int h) {
        height = h;
    }

    int Volume() {
        return getLength() * getBreadth() * height;
    }
};

int main() {
    Cuboid c1(10, 7, 5);
    cout << c1.Volume() << endl;
}
```

## Constructors in Inheritance

When an object of derived class is created,
constructor of the base class is called first, and
then the constructor of derived class is called.

By default, non parameterized constructor of base class is executed.

**Program 1**

```c++
class Base
{
public:
    Base() { cout << "Non-param Base" << endl; }
    Base(int x) { cout << "Param of Base " << x << endl; }
};

class Derived : public Base
{
public:
    Derived() { cout << "Non-Param Derived" << endl; }
    Derived(int y) { cout << "Param of Derived " << y << endl; }
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

```c++

class Base
{
public:
    Base() { cout << "Non-param Base" << endl; }
    Base(int x) { cout << "Param of Base " << x << endl; }
};

class Derived : public Base
{
public:
    Derived() { cout << "Non-Param Derived" << endl; }
    Derived(int y) { cout << "Param of Derived " << y << endl; }
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

Parameterised constructor of base class must be explicitly called from derived class constructor.

```c++
class Base
{
public:
    Base() { cout << "Non-param Base" << endl; }
    Base(int x) { cout << "Param of Base " << x << endl; }
};

class Derived : public Base
{
public:
    Derived() { cout << "Non-Param Derived" << endl; }
    Derived(int y) { cout << "Param of Derived " << y << endl; }

    Derived(int x, int y) : Base(x) // Calling base class constructor explicitly
    {
        cout << "Param of Derived " << y << endl;
    }
};

int main()
{
    Derived d(5, 10);
}
```

Output

```
Param of Base 5
Param of Derived 10
```

## Same method name in Derived Class

```c++

class Employee
{
    int eID;
public:
    void printData() {
        cout << "eID";
    }
};

class Manager: private Employee
{
    string title;
public:
    void printData() {
        cout << "title";
    }

    void printAllDetails() {
        printData();            // "title"
        Employee::printData();  // "eID"
        // To resolve identity we use scope resolution operator
    }
};
```

## Purpose of Inheritance:

1. **Generalization**
   - It is bottom-up approach.
   - Derived classes already exists, but to simplify things we make a generalized Base class.
   - We can use a generalized(same) name for different classes : polymorphic
   - For example, Car - Innova, Swift, Fortuner
     - We only need to learn How to Drive a car, then we can ride any car we want (Innova, Swift, Fortuner)
   - Purpose of Generalization is to achieve `Polymorphism`

2. **Specialization**
   - It is top-down approach.
   - Derived classes are inherited from already existing base class (More specilized version of base class is made)
   - It shares it features to its child classes
   - For example, Rectangle - Cuboid
     - Cuboid inherits the features of Rectangle.
   - Purpose of Specialization is to achieve `Inheritance`

## Base Class Pointer and Derived Class Object

Consider these classes

```c++
class BasicCar
{
public:
    void start() {
        cout << "Car started" << endl;
    }
};

class AdvanceCar : public BasicCar
{
public:
    void playMusic() {
        cout << "Music Playing" << endl;
    }
};
```

**Branch 1**

```c++
void main()
{
    BasicCar *bc;
    bc = new AdvanceCar();
    bc->start();
//  bc->playMusic();            This will generate error
}
```

Once the `BasicCar` pointer is assigned `AdvanceCar` object

then the Pointer will treat the object as if it is a `BasicCar` object.

Hence we **cannot** access the `AdvanceCar` methods.

> **Note:** Data members are accessed **according to the type of pointer** we have. 
> and **NOT according to the object** we have got.
>
> Base Class Pointer can Hold the object of Derived class, 
> But It can only call those methods which are defined in the Base class.
{style="note"}

**Branch 2**

```c++
void main()
{
    AdvanceCar *ac;
    ac = new BasicCar();
}
```

This branch is erroneous.

We can never assign `BasicCar` object to `AdvanceCar` pointer.

Because the `AdvanceCar` pointer is supposed to have `playMusic()` functionality as well,

But we won't get that functionality, because we're trying to assign `BasicCar` object.

## Composition vs Inheritance

Composition is **has-a**.

Inheritance is **is-a**.

### Composition

```c++
class Car : public Engine, public Wheels {};    // ❌ Wrong Design
```

```c++
class Engine {};
class Wheels {};

class Car {
    Engine e;
    Wheels w;
};
```

Car **has-a** Engine.

### Inheritance

```c++
class Animal {};

class Dog: public Animal {};
```

Dog **is-a** Animal.
