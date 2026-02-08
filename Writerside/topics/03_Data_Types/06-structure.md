# Structure
<show-structure depth="2"/>

A structure is a user-defined data type that 
groups related variables of different types under one name. 

```c++
struct Student {
    int id;
    double gpa;
    char grade;
};

// Creating variables
Student s1;
Student s2;
struct Student s3;   // C-style, works but unnecessary in C++
// C++ lets us drop the struct keyword when declaring variables.
```

## Accessing members

We can access using `.` operator:

```c++
s1.id = 101;
s1.gpa = 8.6;
s1.grade = 'A';
```

## Initialization

**Aggregate initialization**

```c++
Student s = {101, 8.6, 'A'};
```

Order matters.

**Designated initializers (C++20)**

```c++
Student s = {
.id = 101,
.gpa = 8.6,
.grade = 'A'
};
```

Readable. Safe. Less chance of swapping GPA with ID and ruining a career.

## Struct with functions

```c++
struct Student {
    int id;
    double gpa;

    void print() {
        cout << id << " " << gpa << endl;
    }
};


Student s{101, 8.6};
s.print();
```

## Structure and Functions

**Passing by value (copy)**

```c++
void print(Student s) {
    cout << s.id;
}
```

Copies everything. Fine for small structs, painful for big ones.

**Passing by reference (recommended)**
```c++
void print(Student& s) {
    cout << s.id;
}
```

### Passing array of structures

```c++
Student sArr[10];

printAll(sArr);
```

Since, it's an array, it will be **passed by reference** only.

### Array within Structure

```c++
struct Student {
    int id;
    double gpa;
    char grade;
    int subjectMarks[10];
};
```

When we pass this structure **by value** to a function, 
then the entire array of the structure will get copied.

## Nested Structures

```c++
struct Address {
    string city;
    int pin;
};

struct Person {
    string name;
    Address addr;
};
```

We can access using `.` operator:
```c++
Person p;
p.addr.city = "Delhi";
```

## Pointer to a Structure

```c++
Student s;
Student *p = &s;

(*p).id = 101;  // sets id of s
p->id = 101;    // sets id of s
```

`p->x` is just shorthand for `(*p).x`

### Dynamic Structures

```c++
Student *p = new Student;
p->id = 101;
delete p;
```

### Self Reference Structures

```c++
struct Employee {
    int eNumber;
    string name;
    Employee *next;
};

Employee e1;
e1.eNumber = 101;
e1.name = "Foo";
e1.next = NULL;

Employee e2;
e2.eNumber = 102;
e2.name = "Bar";
e2.next = &e1;
```

## Structure vs Class

| Feature               | struct   | class     |
|-----------------------|----------|-----------|
| Default access        | `public` | `private` |
| Can have methods      | Yes      | Yes       |
| Can have constructors | Yes      | Yes       |
| Can use inheritance   | Yes      | Yes       |


```c++
struct Example {
    private:
        int c;

    protected:
        int b;

    public:
        int a;
};
```

```c++
struct Base {
    int x;
};

struct Derived : Base {
    int y;
};
```

- struct → public inheritance by default
- class → private inheritance by default
