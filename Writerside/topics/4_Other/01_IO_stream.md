# IO Stream

Stream is flow of data.

They are used for accessing data from outside the program.

I/O Streams are used for input and output data to and from the program.

C++ provides class for accessing input output operations.

Iostream is a base class for all classes.

Istream is for input.

- Cin is the object of istream.

Ostream is for output.

- Cout is an object of ostream.

## Writing in a file

```cpp
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

```cpp
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

Serialization is a process of string and retrieving state of an object.

```cpp
class Student
{
private:
    string name;
    int roll;
    string branch;
public:
    Student(){}
    Student(string n,int r,string b)
    {
        name=n;
        roll=r;
        branch=b;
    }
    friend ofstream & operator<<(ofstream &ofs,Student s);
    friend ifstream & operator>>(ifstream &ifs,Student &s);
    friend ostream & operator<<(ostream &os,Student &s);
};

ofstream & operator<<(ofstream &ofs,Student s)
{
 ofs<<s.name<<endl;
 ofs<<s.roll<<endl;
 ofs<<s.branch<<endl;
 return ofs;
}

ifstream & operator>>(ifstream &ifs,Student &s)
{
 ifs>>s.name;
 ifs>>s.roll;
 ifs>>s.branch;
 return ifs;
}

ostream & operator<<(ostream &os,Student &s)
{
 os<<"Name "<<s.name<<endl;
 os<<"Roll "<<s.roll<<endl;
 os<<"Branch "<<s.branch<<endl;
 return os;
}

int main()
{
    ofstream ofs("Test.txt");
    Student s1("John",10,"CS");

    ofs<<s1;
    ofs.close();

    Student s2;
    ifstream ifs("Test.txt");
    ifs>>s2;

    cout<<s2;
}
```