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
