# Polymorphism
<show-structure depth="2"/>

It is the ability for data or message to be processed in more than one form.

## Function Overloading

When more than one function have the same name, 
but different parameter list, then they are overloaded functions.

- Overloaded function may have:
  1. Different type of parameters
  2. Different number of parameters
  3. Different sequence of parameters

Return type the is not considered in overloading.

**Not Overloaded:**

```c++
void square(int a, int b)
void square(int x, int y)
// Will give redefinition error

int square(int a, int b)
float square(int x, int y)
// Will give redefinition error

void print(char *name);
void print(char name[]);
// Will give redefinition error
```

**Overloaded:**

```c++
void square(int a, int b)
void square(char x, int y)

void square(int a, char b)
void square(char x, int y)

void square(int a, int b)
void square(int x, int y, int z)

void print(char name[]);
void print(char name[][2]);
void print(char name[][2][10]);
```

**Question to solve** Which of the following are overloaded ?

```c++
void function();            // #1
void function(int p);       // #2
void function(int &p);      // #3
void function(int p = 10);  // #4

// Answer A: 1, 2
// Answer B: 1, 3
// Answer C: 4
```

Function overloading is used for achieving **compile time polymorphism**

> Using of default arguments gives appearance of overloading, 
> but using overloading instead of default arguments is more beneficial
{style="note"}

## Operator Overloading

We can define **operator** for our own classes.

Operators can be overloaded using **member functions** or **friend functions**.

> Global functions can access private and protected members 
of an object if they are declared as friend inside a class.
{style="note"}

### Operator overloading using member function

**The problem:**

```c++
class Complex {
public:
    int real;
    int imag;

    Complex(int real = 0, int imag = 0) {
        this->real = real;
        this->imag = imag;
    }

    Complex add(Complex c) {
        Complex temp;
        temp.real = this->real + c.real;
        temp.imag = this->imag + c.imag;
        return temp;
    }
};

int main() {
    Complex c1(10, 5), c2(2, 2), c3;
    
    c3 = c1.add(c2);
    c3 = c2.add(c1); // This would also give the same result
    
    cout << c3.real << "+i" << c3.imag;      => 12+i7
}
```

How easy would it be, to use `+` instead of `add()`, don't you think ?

Let's overload `+` operator for this class.

```c++

class Complex {
public:
    int real;
    int imag;

    Complex(int real = 0, int imag = 0) {
        this->real = real;
        this->imag = imag;
    }

    Complex operator+(Complex c) {
        Complex temp;
        temp.real = this->real + c.real;
        temp.imag = this->imag + c.imag;
        return temp;
    }
};

int main() {
    Complex c1(10, 5), c2(2, 2), c3;
    
    c3 = c1.operator+(c2);  // Statement 1
    c3 = c1 + c2;           // Statement 2
    
    cout << c3.real << " " << c3.imag;      => => 12+i7
}
```

`Statement 1` and `Statement 2` will perform the same operation.

### Operator Overloading using friend function

```c++
class Complex {
    int real;
    int imag;

public:
    Complex(int real = 0, int imag = 0) {
        this->real = real;
        this->imag = imag;
    }

    void display() {
        cout << real << " + i" << imag;
    }

    friend Complex operator+(Complex c1, Complex c2);
};

Complex operator+(Complex c1, Complex c2)
{
    Complex temp;
    temp.real = c1.real + c2.real;
    temp.imag = c1.imag + c2.imag;
    return temp;
}

int main()
{
    Complex c1(10, 5), c2(2, 2), c3;
    c3 = operator+(c1,c2);
    c3 = c1 + c2;
    c3.display();           => 12 + i7
}
```

`friend` function has to be declared inside the class and defined outside the class.

### Overloading Insertion Operator

**The problem:**

```c++
class Complex {
    int real;
    int imag;

public:
    Complex(int real = 0, int imag = 0) {
        this->real = real;
        this->imag = imag;
    }

    void display() {
        cout << real << " + i" << imag;
    }
};

int main() {
    Complex c1(10, 5);
    c1.display();
}
```

How easy would it be, to use `cout <<` instead of `display()`, don't you think ?

Let's overload `<<` operator for this class.

```c++
class Complex {
private:
    int real;
    int imag;

public:
    Complex(int real = 0, int imag = 0) {
        this->real = real;
        this->imag = imag;
    }

    friend ostream& operator<<(ostream&, Complex c);
};

ostream& operator<<(ostream& out, Complex c) {
    out << c.real << " + i" << c.imag;
    return out;
}

int main() {
    Complex c1(10, 5);
    cout << c1;
}
```

We can observe that `operator<<()` function 
is getting two parameters of different classes (ostream class and Complex class).

So we have to make it as a `friend` function.

## Function Overriding

When a derived class function has the same name as of the bass class' function,
Then derived class member function hides the base class' inherited function,
And this situation is called function overriding.

```c++
class BasicCar
{
public:
    void start() { cout << "BasicCar" << endl; }
};

class AdvanceCar : public BasicCar
{
public:
    void start() { cout << "AdvanceCar" << endl; }
};

int main()
{
    BasicCar* b = new BasicCar();
    b->start();                   // "BasicCar"

    AdvanceCar* d = new AdvanceCar();
    d->start();                   // "AdvanceCar"

    // Base class pointer assumes that it's pointing to the base class object,
    // so It will only access the base class methods.
    BasicCar* b = new AdvanceCar();
    b->start();                   // "BasicCar"
    // It didn't call Derived Class method, even though it's been overridden
}
```

For non-virtual functions, C++ uses static binding (Compile time):

The function to call is decided **based on the pointer type, not the object type**.

### Virtual Functions

```c++
class BasicCar
{
public:
    // Virtual function
    virtual void start() { cout << "BasicCar" << endl; }
};

class AdvanceCar : public BasicCar
{
public:
    void start() { cout << "AdvanceCar" << endl; }
};

int main()
{
    // base pointer → derived object
    BasicCar* b = new AdvanceCar();
    b->start();                                 // "AdvanceCar"
    // runtime decision 
    
    //----------------------------------------------------------
    
    BasicCar *b;
    AdvanceCar d;
    
    b = &d; // base pointer → derived object
    b->start();                                 // "AdvanceCar"
    // runtime decision 
}
```

- **When:**
  1. The `Base` class function is declared `virtual`, and it is overridden in derived class.
  2. And the `Base` class pointer is pointing to the `Derived` class object.

**Then:**
The function call `b->start()` is resolved at runtime 
because `start()` is virtual and invoked via a base class pointer/reference, 
and the decision is made using the actual object type through dynamic dispatch.

> The function call will be **resolved at runtime**, 
> based on the **actual object type, not the pointer type**.
> 
> Hence, it is called **runtime polymorphism**.
{style="note"}
