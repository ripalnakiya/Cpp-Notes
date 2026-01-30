# Template Class

They can work for any type of data

**Program 1 : `int` specific class for stack**

```cpp
class Stack
{
private:
    int *stk;
    int top;
    int size;

public:
    Stack(int sz)
    {
        size = sz;
        top = -1;
        stk = new int[size];
    }
    void push(int x);
    int pop();
};
void Stack::push(int x)
{
    if (top == size - 1)
        cout << "Stack is Full";
    else
    {
        top++;
        stk[top] = x;
    }
}
int Stack::pop()
{
    int x = 0;
    if (top == -1)
        cout << "Stack is Empty" << endl;
    else
    {
        x = stk[top];
        top--;
    }
    return x;
}
void main()
{
    Stack s(10);
    s.push(10);
    s.push(23);
    s.push(33);
}
```

**Program 2 : generic class for stack**

```cpp
template <class T>
class Stack
{
private:
    T *stk;
    int top;
    int size;

public:
    Stack(int sz)
    {
        size = sz;
        top = -1;
        stk = new T[size];
    }
    void push(T x);
    T pop();
};

template <class T>
void Stack<T>::push(T x)
{
    if (top == size - 1)
        cout << "Stack is Full";
    else
    {
        top++;
        stk[top] = x;
    }
}

template <class T>
T Stack<T>::pop()
{
    T x = 0;
    if (top == -1)
        cout << "Stack is Empty" << endl;
    else
    {
        x = stk[top];
        top--;
    }
    return x;
}

void main()
{
    Stack<int> s(10);
    s.push(10);
    s.push(23);
    s.push(33);
}
```
