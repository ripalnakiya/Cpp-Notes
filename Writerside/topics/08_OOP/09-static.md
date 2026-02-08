# Static
<show-structure depth="2"/>

## Static Variables

- **Scope:** Limited to the block/function where it’s declared
- **Lifetime:** Entire program (exists from start to end)
- Value persists across function calls

<br></br>

- **Use cases:**
  - Counting function calls
  - Caching values
  - Maintaining state without global variables

```c++
void fun()
{
    static int v = 0;
    int a = 10;
    v++;
    cout << a << " " << v;
}

int main()
{
    fun(); // 10 1
    fun(); // 10 2
    fun(); // 10 3
}
```

## Static Data Members

```c++
class Student {
public:
    static int totalStudents;   // Declaration
};

int Student::totalStudents = 0; // Definition
```

- Only one copy exists for the entire class
- Shared by all objects
- Not tied to any specific instance, can be accessed directly using class name.

**Lifetime:** Exists for the entire program (Created once, destroyed at program end)

## Static Member Functions

Static members functions are functions of a class, they can be called using class name, without
creating object of a class.

They can access only static data members of a class, they cannot access non-static members
of a class.

```c++
class Math {
public:
    static int add(int a, int b) {
        return a + b;
    }
};
```

- Belong to the class, not to objects (Hence, No `this` pointer)
- Can be called without creating an object
- Cannot access non-static members
- Can only access:
  - Static data members
  - Other static functions

## Static Example

```c++
class Test
{
private:
    int a;
    static int count;

public:
    Test() {
        a = 10;
        count++;
    }

    static int getCount() {
        return count;
    }
};

int Test::count = 0;

int main()
{
    Test t1, t2;
    
    cout << Test::getCount();   // 2
    
    cout << t1.getCount();      // 2
    // No harm in calling it using a object
}
```
