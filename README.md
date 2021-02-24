# Binary Search Simulation

Python program to visualize the behavior of upper_bound and lower_bound binary searches.

<table>
  <tr>
    <th>Upper Bound</th>
    <th>Lower Bound</th>
  </tr>
  <tr>
    <td>
      <img src="https://searleser97.github.io/BinarySearchSimulation/upper_bound.png" width="250" height="400" />
    </td>
    <td>
      <img src="https://searleser97.github.io/BinarySearchSimulation/lower_bound.png" width="250" height="400" />
    </td>
  </tr>
</table>

<table>
<tr>
<th>Upper Bound</th>
<th>Lower Bound</th>
</tr>
<tr>
<td>

```cpp
int upperBound(vector<int> &array, int target) {
  // array should be sorted in non-decreasing
  // order from left to right
  int l = 0, r = array.size() - 1;
  while (l <= r) {
    int mid = l + (r - l) / 2;
    if (target < array[mid]) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
  return l;
}
```

</td>
<td>

```cpp
int lowerBound(vector<int> &array, int target) {
  // array should be sorted in non-decreasing
  // order from left to right
  int l = 0, r = array.size() - 1;
  while (l <= r) {
    int mid = l + (r - l) / 2;
    if (target <= array[mid]) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
  return l;
}
```

</td>
</tr>
</table>

<table>
<tr>
<th colspan="2">Binary Search Variation (works optimally for non-integer spaces)</th>
<tr>
<th>Upper Bound</th>
<th>Lower Bound</th>
</tr>
<tr>
<td>

```cpp
int upperBound(vector<int> &array, int target) {
  // array should be sorted in non-decreasing
  // order from left to right
  int l = -1, r = array.size();
  while (l + 1 < r) {
    int mid = l + (r - l) / 2;
    if (target < array[mid]) {
      r = m;
    } else {
      l = m;
    }
  }
  return r;
}
```

</td>
<td>

```cpp
int lowerBound(vector<int> &array, int target) {
  // array should be sorted in non-decreasing
  // order from left to right
  int l = -1, r = array.size();
  while (l + 1 < r) {
    int mid = l + (r - l) / 2;
    if (target <= array[mid]) {
      r = m;
    } else {
      l = m;
    }
  }
  return r;
}
```

</td>
</tr>
</table>
