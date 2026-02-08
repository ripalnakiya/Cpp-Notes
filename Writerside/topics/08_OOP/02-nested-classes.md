# Nested Classes
<show-structure depth="2"/>

Nested class works exactly the same as any other class, 
similar to declared outside the outer class.

```c++
class Outer {
public:
    class Inner {
    public:
        void hello();
    };
};

void Outer::Inner::hello() {
    // ....
}

Outer::Inner obj;
obj.hello();
```

> A nested class is NOT automatically tied to an object of the outer class.
>
>It is just scoped inside the outer class.
{style="note"}

## Access rules

None of the classes can access other's members directly.

```c++
class Outer {
public:
    int x;
    
    class Inner {
    public:
        void f() {
            x = 10;  // ❌ ERROR
        }
    };
};
```

```c++
class Outer {
public:
    class Inner {
    public:
        int y = 5;
    };

    void f() {
        y = 10; // ❌ ERROR
    }
};
```

It needs object of the class, to access the members.

```c++
class Outer {
public:
    int x = 10;    
    class Inner {
    public:
        void f() {
            Outer o;
            o.x = 20; // ✅ allowed if access permits
        }
    };
};
```

```c++
class Outer {
public:
    class Inner {
    public:
        int y;
    };

    void f() {
        Inner i;
        i.y = 20;   // ✅ allowed if access permits
    }
};
```

### Static Members

Both (Outer and Inner class) can directly access the static members of each other.

```c++
class Outer {
public:
    static int s;

    class Inner {
    public:
        static void f() {
            Outer::s = 10;   // ✅ direct access, no Outer object
        }
    };
};

int Outer::s = 0;
```

```c++
class Outer {
public:
    class Inner {
    public:
        static int y;
    };

    static void f() {
        Inner::y = 7;   // ✅ direct access, no Inner object
    }
};

int Outer::Inner::y = 0;
```

## Access specifiers of nested classes

A nested class itself can be `public`, `protected`, or `private`.

```c++
class Outer {
private:
    class Secret {};
public:
    class PublicOne {};
};
```

Usage:
```c++
Outer::Secret s; // ❌ private
Outer::PublicOne p; // ✅
```

## Implicitly Static Nested Class

In C++, nested classes behave like static members of the outer class, 
even though you never write the word `static`.

- Meaning:
  - They do not need an instance of `Outer`
  - They do not carry outer object state

```c++
class Outer {
public:
    class Inner {
    public:
        void f() {}
    };
};

Outer::Inner obj;
obj.f();
```

`Inner` is not attached to any `Outer` object.

In case of Java language:

```Java
Outer outer = new Outer();
Outer.Inner inner = outer.new Inner();
```
