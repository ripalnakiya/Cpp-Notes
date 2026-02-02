# Vector Of

## Vector of pairs

```c++
vector<pair<int,int>> vp;

vector<pair<int, int>> vp = {{1, 2}, {2, 4}, {3, 6}};

vp.push_back(make_pair(x, y));
vp.push_back({x, y});

cout << v[i].first << " " << v[i].second;
```

### Iterator to vector of pairs

```c++
vector<pair<int, int>> :: iterator it;

for(it = vp.begin(); it!= vp.end(); it++)
    cout << (*it).first << " " << (*it).second;

for(it = vp.begin(); it!= vp.end(); it++)
    cout << it->first << " " << it->second;
```

### Optimize the iterators

```c++
// This copies every pair into value, and then prints it
for(pair<int, int> value : vp)
    cout << value.first << " " << value.second;

// We can use references to directly access the pairs
for(pair<int, int> &value : vp)
    cout << value.first << " " << value.second;

// We can use auto keyword to define the data type
for(auto &value : vp)
    cout << value.first << " " << value.second;
```

## Array of vectors

Array of Vectors is 2D array,
where number of rows are fixed by array size,
but number of columns are not fixed due to vector.

```c++
vector<int> arr[3];

// each arr[i] represents a vector
arr[0] is a vector
arr[1] is a vector
arr[2] is a vector

arr[0] -> 1 2 3
arr[1] -> 2 4 6
arr[2] -> 1 4 9 16 25
```

## Vector of vectors

Vector of vectors can be a 2D vector,
Where neither number of rows are not fixed
nor number of columns are not fixed.

```c++
vector<vector<int>> v;
vector<vector<int>> v = {{1, 0, 0, 0}, {1, 1, 0, 0}, {1, 1, 0, 0}, {0, 1, 1, 1}};

// Initialize vector of (rows * cols) with 0
vector<vector<int>> v(rows, vector<int>(cols, 0));;

int rows = v.size();
int cols = v[0].size();
```

There can variable lengths of each `vector` inside the main `vector` 
(i.e. different column count for each row)
