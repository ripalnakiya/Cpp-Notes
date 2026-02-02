# IO Stream

Stream is flow of data.

They are used for accessing data from outside the program.

I/O Streams are used for input and output data to and from the program.

`iostream` is a base class for all classes.

`istream` is for input. `cin` is the object of `istream`.

`ostream` is for output. `cout` is an object of `ostream`.

## Writing to a file

```c++
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ofstream file("myfile.txt", ios::trunc);

    file << "John" << endl;
    file << 21 << endl;
    file << CSE << endl;

    file.close();
}
```

## Reading from a file

```c++
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream file("myfile.txt");

    if(file.is_open())
        cout << "File is Opened" << endl;

    string name;
    int roll;
    string branch;

    file >> name >> roll >> branch;

    if(file.eof())
        cout << "End of file reached" <<endl;

    file.close();

    cout << "Name: " << name << endl;
    cout << "Roll NO: " << roll << endl;
    cout << "Branch: " << branch << endl;
}
```

## Serialization

**Serialization** is the process of converting an object’s state 
into a format that can be stored or transmitted.

**Deserialization** is the part where we retrieve 
and rebuild the object from that format.

Serialization converts an object into a byte stream, JSON, XML, etc., 
so it can be stored or transmitted 
and later reconstructed via deserialization.

```c++
#include <iostream>
#include <fstream>
using namespace std;

class Student
{
    string name;
    int roll;
    string branch;

public:
    Student(){}
    
    Student(string n, int r, string b)
    {
        name = n;
        roll = r;
        branch = b;
    }

    friend ofstream& operator<<(ofstream& ofs, Student s);
    friend ifstream& operator>>(ifstream& ifs, Student& s);
    friend ostream& operator<<(ostream& os, Student& s);
};

ofstream& operator<<(ofstream& ofs, Student s)
{
    ofs << s.name << endl;
    ofs << s.roll << endl;
    ofs << s.branch << endl;
    return ofs;
}

ifstream& operator>>(ifstream& ifs, Student& s)
{
    ifs >> s.name;
    ifs >> s.roll;
    ifs >> s.branch;
    return ifs;
}

ostream& operator<<(ostream& os, Student& s)
{
    os << "Name " << s.name << endl;
    os << "Roll " << s.roll << endl;
    os << "Branch " << s.branch << endl;
    return os;
}

int main()
{
    ofstream ofs("Test.txt");
    Student s1("John", 10, "CS");
    ofs << s1;
    ofs.close();

    Student s2;
    ifstream ifs("Test.txt");
    ifs >> s2;
    cout << s2;
}
```