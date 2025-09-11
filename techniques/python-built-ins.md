# Python Built-ins Reference

## Tier 1: Absolute Must-Know

### Collections & Data Structures

```python
# Basic operations
len(obj)           # O(1) for most built-ins
list(), set(), dict(), tuple()
sorted(iterable)   # O(n log n), returns new list
obj.sort()         # O(n log n), in-place for lists
```

### String Methods

```python
str.split()        # O(n)
str.join(iterable) # O(n) 
str.strip()        # Remove whitespace
str.replace(old, new)  # O(n)
```

### Iteration & Enumeration

```python
enumerate(iterable)     # Get (index, value) pairs
zip(iter1, iter2)      # Combine iterables
range(start, stop, step)
reversed(iterable)     # O(n) iterator
```

### Math & Comparisons

```python
min(iterable), max(iterable)  # O(n)
sum(iterable)                 # O(n)
abs(x)                        # Absolute value
divmod(a, b)                  # Returns (quotient, remainder)
```

## Tier 2: Very Important

### Advanced Iteration

```python
all(iterable)      # True if all elements are truthy
any(iterable)      # True if any element is truthy
filter(func, iterable)  # Filter elements
map(func, iterable)     # Apply function to all elements
```

### Type Checking & Conversion

```python
isinstance(obj, type)   # Check object type
int(x), float(x), str(x)  # Type conversions
ord(char), chr(num)     # Character ↔ ASCII
```

### Useful Utilities

```python
pow(base, exp, mod)    # Efficient modular exponentiation
round(x, digits)       # Rounding numbers
```

## Tier 3: Standard Library (Import Required)

### Collections Module

```python
from collections import Counter, defaultdict, deque

Counter(iterable)      # Count frequencies - O(n)
defaultdict(factory)   # Dict with default values
deque()               # Double-ended queue - O(1) both ends
```

### Heap Operations

```python
import heapq

heapq.heappush(heap, item)    # O(log n)
heapq.heappop(heap)           # O(log n)  
heapq.heapify(list)           # O(n) - convert list to heap
heapq.nlargest(k, iterable)   # O(n log k)
heapq.nsmallest(k, iterable)  # O(n log k)
```

### Binary Search

```python
import bisect

bisect.bisect_left(arr, x)    # O(log n) - leftmost position
bisect.bisect_right(arr, x)   # O(log n) - rightmost position
bisect.insort(arr, x)         # O(n) - insert in sorted order
```

### String & Math

```python
import string
string.ascii_lowercase    # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase    # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

import math
math.ceil(x), math.floor(x)   # Ceiling/floor
math.gcd(a, b)                # Greatest common divisor
math.sqrt(x)                  # Square root
```