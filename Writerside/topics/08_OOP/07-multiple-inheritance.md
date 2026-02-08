# Multiple Inheritance
<show-structure depth="2"/>

A class inherits from more than one base class.

```c++
class A {
public:
    void foo() {}
};

class B {
public:
    void bar() {}
};

class C : public A, public B {
};

// C gets everything public/protected from both A and B.
C obj;
obj.foo(); // from A
obj.bar(); // from B
```

## Why to use Multiple Inheritance ?

**Mix independent capabilities**

```c++
class Flyable {
public:
    void fly();
};

class Swimmable {
public:
    void swim();
};

class Duck : public Flyable, public Swimmable {
};
```

## Diamond Problem

```c++
class Animal {
public:
    int age;
};

class Mammal : public Animal {};
class Bird   : public Animal {};

class Bat : public Mammal, public Bird {};
```

```
````````Animal
       /      \
  Mammal      Bird
       \      /
          Bat

```

```c++
Bat b;
b.age = 5; // 💥 ERROR: ambiguous
```

- **Why?** Because Bat contains two copies of `Animal`.
  1. One via `Mammal`
  2. One via `Bird`

C++ refuses to guess which `age` you meant.

## Virtual Inheritance

There should be only one shared `Animal`, no matter how we get there.

```c++
class Animal {
public:
    int age;
};

class Mammal : virtual public Animal {};
class Bird   : virtual public Animal {};

class Bat : public Mammal, public Bird {};
```

```c++
Bat b;
b.age = 5; // ✅ works
```

Only one `Animal` subobject exists.

When virtual inheritance is involved, 
the virtual base class is constructed by the most-derived class (`bat` here), 
not by the intermediate base classes.

```c++
class Mammal : virtual public Animal {
public:
    Mammal() : Animal(10) {}
};

class Bird : virtual public Animal {
public:
    Bird() : Animal(20) {}
};

class Bat : public Mammal, public Bird {
};
```

- If both `Mammal` and `Bird` could initialize `Animal`, then:
  - Which constructor should run?
  - `Animal(10)` or `Animal(20)`?
  - Both? That’s illegal.
  - Pick one? That’s arbitrary.

So the language makes a rule: **The most-derived class initializes the virtual base.**

### Initializing virtual base class

```c++
class Animal {
public:
    int age;

    Animal(int a) : age(a) {
        std::cout << "Animal constructed\n";
    }
};

class Mammal : virtual public Animal {
public:
    Mammal() : Animal(10) {   // ❌ ignored
        std::cout << "Mammal constructed\n";
    }
};

class Bird : virtual public Animal {
public:
    Bird() : Animal(20) {     // ❌ ignored
        std::cout << "Bird constructed\n";
    }
};

class Bat : public Mammal, public Bird {
public:
    Bat() : Animal(42), Mammal(), Bird() {
        std::cout << "Bat constructed\n";
    }
};
```

Construction order:

```
1. Animal(42) ← constructed ONCE, here
2. Mammal
3. Bird
4. Bat
```

## Other Ambiguity

Even without shared bases, name clashes can happen.

```c++
class A {
public:
    void f();
};

class B {
public:
    void f();
};

class C : public A, public B {};
```

```c++
C obj;
obj.f(); // ❌ ambiguous
```

**Solution 1: Scope resolution**
```c++
obj.A::f();
obj.B::f();
```

**Solution 2: Override**
```c++
class C : public A, public B {
public:
    void f() {
        A::f(); // or custom logic
    }
};
```
