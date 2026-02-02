# Exception Handling

```c++
#include <iostream>
using namespace std;

int division(int x, int y)
{
    if (y == 0)
        throw 1;
    return x / y;
}

int main()
{
    int a = 10, b = 2, c;
    try
    {
        c = division(a, b);
        cout << c << endl;
    }
    catch (int err)
    {
        cout << "Division failed: " << err << endl;
    }
    catch (...)
    {
        cout << "Catch all exceptions" << endl;
    }
    return 0;
}
```