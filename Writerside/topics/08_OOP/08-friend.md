# Friend

## Friend Function

They are the non-member functions 
that can **access** and manipulate the **private and protected members** 
of the class.

They can access members of a class using the object.

A friend function can be:
1. Global function
2. Member function of another class

```c++

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
    
    a = 15; // We need a object to access, 
            // directly trying to access a member will generate error
}
```

## Friend Class

It can access private and protected member**s** of other classes 
in which it is declared as a friend.

All the functions of friend class can 
access private and protected members of other class.

```c++
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
};
```

## Nested Classes

### Accessing private variables of outer class

```c++
class Outer {
    int x = 10;
    friend class Inner;   // grant access

public:
    class Inner {
    public:
        void f(Outer& o) {
            o.x = 20;   // ✅ now allowed
        }
    };
};
```

### Accessing private variables of inner class

```c++
class Outer {
public:
    class Inner {
        int y = 20;
        friend class Outer; // grant access
    };
    
    void function(Inner& i) {
        i.y = 200;   // ✅ now allowed
    }
};
```
