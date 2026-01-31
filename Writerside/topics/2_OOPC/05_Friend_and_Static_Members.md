# Friend and Static Members

## Friend

### Friend Function

They are the non-member functions that can access and manipulate the private and protected members of the class for they are declared as friends.

They can access member of a class upon their objects

A friend function can be:

- global function
- member function of another class

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
    // a = 15;      Directly trying to access data member will generate error
}
```

we can access private and protected members of the class using a object inside the friend function

### Friend Class

A friend class can access private and protected members of other classes in which it is declared as a friend.

All the functions of friend class can access private and protected members of other class

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
}
```

## Static

### Static Data Member

Static data members are members of a class.

Only one instance of static members is created and shared by all objects.

They can also be accessed directly using class name.

### Static Member Function

Static members functions are functions of a class, they can be called using class name, without
creating object of a class.

They can access only static data members of a class, they cannot access non-static members
of a class.

### Example

```c++
class Test
{
private:
    int a;
    static int count;
public:
    Test()
    {
        a=10;
        count++;
    }
    static int getCount()
    {
        return count;
    }

};

int Test::count=0;

int main()
{
    Test t1,t2;
    cout<<t1.getCount()<<endl;
    // t1.count=10;                 This can also be done, if the static data member is public
    cout<<Test::getCount()<<endl;
}
```

**Uses**

- Static members can be used as a counter
- They can be used as a shared memory for all the objects
- They can Provide about a class

## Nested class

Firstly, the Nested class works exactly the same as any other class, declared outside of the outer class.

Inner class can access the static members of outer class.

Object of Inner class can be created inside the outer class.

Outer class can access all the public member is Inner class(using its object).

```c++
class Outer
{
    public:
        void fun()
        {
            i.display();            // Using members of Inner class
        }

        class Inner
        {
            public:
                void display()
                {
                    cout<< "Display of Inner"<<endl;
                }
        };
        Inner i;                    // Creating object of Inner class
};

void main()
{
    Outer o1;                                       // Creating object of Outer class
    o1.fun();               => Display of Inner
    Outer::Inner i1;                                // Creating object of Inner class
    i1.display();           => Display of Inner
}
```