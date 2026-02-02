# Preprocessors

Preprocessors are instructions to the compiler.

They are processed before compilation (replacement is performed before the compilation).

**They are used for:**
  - defining symbolic constants
  - defining functions
  - conditional operations

Preprocessor Directives are also called **Macros**.

## Symbolic Directives

```c++
#define PI 3.14

int main()
{
    cout << PI; // 3.14
}
```

```c++
#define PI 3.14
#define PI 3

int main()
{
    cout << PI; // 3
}
```

## Functional Directives

```c++
#define maxi(a,b) (a > b ? a : b)

int main()
{
    cout << maxi(10, 12); // 12
}
```

```c++
#define msg(x) #x

int main()
{
    cout << msg(Hello); // Hello
}
```

`#` before `x` makes the value of `x` as string 
(It wraps the value of `x` in double quotes).

## Conditional Directives

`ifndef` - If not defined

```c++
#define PI 3.14

#ifndef PI
    #define PI 3
#endif

int main()
{
    cout << PI; // 3.14
}
```

If value of `PI` is not defined already, then it will get executed.

```c++
#ifndef PI
    #define PI 3
#endif

int main()
{
    cout << PI; // 3
}
```
