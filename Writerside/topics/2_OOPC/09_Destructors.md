# Destructors

Constructors are used for acquiring the resources.

Destructors are used for releasing the resources acquired by object of the class.

```c++
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

```c++
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

```c++
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

```c++
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

```c++
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

```c++
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

```c++
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