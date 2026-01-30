# Operator Overloading

We can define operator for our own classes.

Operators can be overloaded using member functions or friend functions.

Global functions can also access private and protected members of an object if they are
declared as friend inside a class.

First, let us see basic function

```cpp
class Complex
{
public:
    int real;
    int imag;

    Complex(int real = 0, int imag = 0)
    {
        this->real = real;
        this->imag = imag;
    }

    Complex add(Complex c)
    {
        Complex temp;
        temp.real = this->real + c.real;
        temp.imag = this->imag + c.imag;
        return temp;
    }
};

void main()
{
    Complex c1(10, 5), c2(2, 2), c3;
    c3 = c1.add(c2);
//  c3 = c2.add(c1);                                This would also give the same result
    cout << c3.real << "+i" << c3.imag << endl;     => 12+i7
}
```

Now let us see how operators are overloaded.

```cpp
class Complex
{
public:
    int real;
    int imag;

    Complex(int real = 0, int imag = 0)
    {
        this->real = real;
        this->imag = imag;
    }

    Complex operator+(Complex c)
    {
        Complex temp;
        temp.real = this->real + c.real;
        temp.imag = this->imag + c.imag;
        return temp;
    }
};

void main()
{
    Complex c1(10, 5), c2(2, 2), c3;
//  c3 = c1.operator+(c2);                             Statement 1
    c3 = c1 + c2;                                   // Statement 2
    cout << c3.real << " " << c3.imag << endl;      => 12+i7
}
```

`Statement 1` and `Statement 2` will perform the same operation.

## Operator Overloading using friend function

```cpp
class Complex
{
private:
    int real;
    int imag;

public:
    Complex(int real = 0, int imag = 0)
    {
        this->real = real;
        this->imag = imag;
    }

    void display()
    {
        cout << real << " + i" << imag << endl;
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

void main()
{
    Complex c1(10, 5), c2(2, 2), c3;
    // c3 = operator+(c1,c2);
    c3 = c1 + c2;
    c3.display();                               => 12 + i7
}
```

`friend` function has to be declared inside the class and defined outside the class.

## Overloading Insertion Operator

First let's see a basic display function

```cpp
class Complex
{
private:
    int real;
    int imag;

public:
    Complex(int real = 0, int imag = 0)
    {
        this->real = real;
        this->imag = imag;
    }

    void display()
    {
        cout << real << " + i" << imag << endl;
    }
};

void main()
{
    Complex c1(10, 5);
    c1.display();
}
```

Now let us see Inseration Operator Overloading

```cpp
class Complex
{
private:
    int real;
    int imag;

public:
    Complex(int real = 0, int imag = 0)
    {
        this->real = real;
        this->imag = imag;
    }

    friend ostream &operator<<(ostream &, Complex c);
};

ostream &operator<<(ostream &out, Complex c)
{
    out << c.real << " + i" << c.imag;
    return out;
}

void main()
{
    Complex c1(10, 5);
    cout << c1;
}
```

We can observe that fucntion operator<<() function is getting two parameters of different classes (ostream class and Complex class).

So we has to make it as a friend function.