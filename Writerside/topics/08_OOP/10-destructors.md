# Destructors

Constructors are used for acquiring the resources.

Destructors are used for releasing the resources acquired by object of the class.

- It will have same name as class name, with `~` symbol.
- It will not have a return type.
- It is invoked automatically when object goes out of scope.
- If it is not defined then class will generate a destructor.
- We can have only one destructor in a class, (Can't be overloaded).

> Only those functions that have access to both constructor and destructor of a class,
> can create object of that class.

```c++
class Demo {
public:
    Demo() {
        cout<< "Constructor is Called" << endl;
    }
    ~Demo() {
        cout<< "Destructor is Called" << endl;
    }
};

int main() {
    Demo d;
}
```

**Output**

```
Constructor is Called
Destructor is Called
```

- Constructor is called when the object is created.
- Destructor is called when the object goes out of scope.


## Destructors with Dynamic Objects

```c++
class Demo {
public:
    Demo() {
        cout<< "Constructor is Called" << endl;
    }
    ~Demo() {
        cout<< "Destructor is Called" << endl;
    }
};

int main() {
    Demo *d = new Demo();
}
```

**Output**

```
Constructor is Called
```

When we create object dynamically using `new` operator,
only the constructor is called.

We need to delete the object explicitly using `delete` operator,
and that will call the destructor.

```c++
class Demo {
public:
    Demo() {
        cout<< "Constructor is Called" << endl;
    }
    ~Demo() {
        cout<< "Destructor is Called" << endl;
    }
};

int main() {
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
class Demo {
    int *ptr;
public:
    Demo() {
        ptr = new int[10];
        cout<< "Constructor is Called" << endl;
    }
    ~Demo() {
        delete []ptr;
        cout<< "Destructor is Called" << endl;
    }
};

int main() {
    Demo *d = new Demo();
    delete d;
}
```

**Output**

```
Constructor is Called
Destructor is Called
```

When object is deleted,
the memory(resources) acquired by it should also be deleted.

So we can include those operators in the destructor.


## Destructors in Inheritance

```c++
class Base {
public:
    Base() {
        cout << "Constructor Base" << endl;
    }
    ~Base() {
        cout << "Destructor Base" << endl;
    }
};

class Derived : public Base {
public:
    Derived() {
        cout << "Constructor Derived" << endl;
    }
    ~Derived() {
        cout << "Destructor Derived" << endl;
    }
};

int main() {
    Derived d;
}
```

**Output**

```
Constructor Base
Constructor Derived

Destructor Derived
Destructor Base
```

### Destructor of polymorphic class

Using a class **polymorphically** means
interacting with derived objects through a base-class interface
and expecting runtime behavior based on the actual derived type.

```c++
class Base {
public:
    Base() {
        cout << "Constructor Base" << endl;
    }
    ~Base() {
        cout << "Destructor Base" << endl;
    }
};

class Derived : public Base {
public:
    Derived() {
        cout << "Constructor Derived" << endl;
    }
    ~Derived() {
        cout << "Destructor Derived" << endl;
    }
};

int main() {
    Base *ptr = new Derived();
    // Some processing
    delete ptr;
}
```

**Output**

```
Constructor Base
Constructor Derived

Destructor Base
```

It does not call the destructor of `Derived` class,
since pointer assumes that it holds a `Base` class object.

### Virtual Destructor

```c++
class Base {
public:
    Base() {
        cout << "Constructor Base" << endl;
    }
    virtual ~Base() { // Creates a user-defined virtual destructor
        cout << "Destructor Base" << endl;
    }
};

class Derived : public Base {
public:
    Derived() {
        cout << "Constructor Derived" << endl;
    }
    ~Derived() {
        cout << "Destructor Derived" << endl;
    }
};

int main() {
    Base *ptr = new Derived();
    // Some processing
    delete ptr;
}
```

**Output**

```
Constructor Base
Constructor Derived

Destructor Derived
Destructor Base
```

We should make the destructor `virtual` if:
- The class is intended to be **used polymorphically**
- You ever plan to **delete derived objects via a base pointer**
- The class **has any virtual function** (strong rule of thumb)

```c++
class Drawable {
public:
    virtual void draw() {   // virtual function
        cout << "Drawable draw()";
    }
    
    virtual ~Drawable() {};
    // Creates a user-defined virtual destructor
    
    virtual ~Drawable() = default;  
    // Compiler generates the destructor automatically
};
```
