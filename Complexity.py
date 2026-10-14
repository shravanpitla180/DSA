'''
Time & Space Complexity:-

Time Complexity :--> It analyz how the amount (or) time grows as the input size grows.

Space Complexity(Memory) :--> IT analyze memory needs for an algorithm as input grows.

---!!!---Time Complexity---!!!---
---Types of Levels---
1.Constant Time -> O(1):-Accessing index value.

2.Linear Time -> O(n):-Accessing every value in a list
ex:- when using a single for loop
nums = [10, 20, 30, 40]
for num in nums:
    print(num)

3.Logarithmic Time -> O(logn) :-->It repeatedly reduces the problem size by a constant factor 
--> Binary Search --> The technique we use (Divide and conquer)
-->[10,20,30,40,50] first separate array into left,  right and middle ,then compare middle value ( if a[mid] == target: return mid)  
                             and also compare with other operator if satisfy <-(left mid+1) , >=(right mid-1),
                             then next index changes to condition  it satisfy.. 
        -> ex: if a[mid] ==  target:
                      return mid
               elif a[mid] < target:
                      return mid+1  (left)
               elif a[mid] > target:
                      return mid-1  (right)
               else:
                      return i-1

4.Quadratic Time ->O(n^2) :-->Order of n square times Complexity
-->Nested loop
Ex:-for i in l:
        for j in l:
            print(i*j)

5.Linearithmic Time -> O(n log n) --> Order of n log n
O(n) + O(log n)
O(n) --> Checking each element.
O(log n) --> Divide & conquer.
ex:- Selection sort, Insertion sort

6.Exponential Time -> O(2^n) :--> one function calling multiple times
-->Fibonacci series.

7.Factorial Time - O(n!) --> Travelling salesman Problem.
-->Finding all permutations of distinct elements.

-----Levels-----
O(1) -> O(log n) -> O(n) -> O(n log n) -> O(n^2) -> O(2^n) -> O(n!).

'''
def constant(n):
    """O(1): Constant time — work stays the same as n grows."""
    return n * 2                         # Example: one calculation


def logarithmic(n):
    """O(log n): Logarithmic time — the problem size shrinks by a factor each step."""
    count = 0
    while n > 1:
        n //= 2                          # Example: repeatedly halve n
        count += 1
    return count


def linear(n):
    """O(n): Linear time — work grows in proportion to n."""
    total = 0
    for number in range(n):              # Example: visit each item once
        total += number
    return total


def linearithmic(n):
    """O(n log n): Linearithmic time — commonly seen in efficient sorting."""
    if n <= 1:
        return
    middle = n // 2
    linearithmic(middle)                 # Split into smaller parts
    linearithmic(n - middle)             # Process both parts
    for _ in range(n):                   # Then do O(n) work
        pass
    # This demonstrates the recurrence T(n) = 2T(n/2) + O(n).


def quadratic(n):
    """O(n²): Quadratic time — work grows like n multiplied by n."""
    for i in range(n):
        for j in range(n):               # Example: compare every pair
            pass


def exponential(n):
    """O(2ⁿ): Exponential time — each step branches into two choices."""
    if n <= 0:
        return 1
    return exponential(n - 1) + exponential(n - 1)
    # Example: simple recursive branching; very slow for larger n.


def factorial(n):
    """O(n!): Factorial time — tries every ordering of n items."""
    def permute(items, start):
        if start == len(items):
            return
        for i in range(start, len(items)):
            items[start], items[i] = items[i], items[start]
            permute(items, start + 1)
            items[start], items[i] = items[i], items[start]

    permute(list(range(n)), 0)
    # Example: generate all permutations (n! possibilities).


'''
---!!!---Space Complexity---!!!---
---Types of Levels---
1.constant Auxillary space - O(1):
--> creating a variable and assigning value to it.
--> Memory usage stays approximately constant as the input grows.

2.Linear Auxillary space - O(n): 
--> creating seprate list to store.
--> Memory usage grows with the input size.
example:-
nums = [1,2,3,4,5]
square = []
for num in nums:
    square.append(num * num)
print(square)

3.Quadratic Auxillary space - O(n^2)
--> Matrix Array
--> Memory usage grows proportionally to the square of the input size.
->EX:--Nested Loops
example:-
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix
print(create_matrix(3))

'''
def constant_space(items):
    """O(1): Constant extra space—uses a fixed amount of memory.
    Example: find a maximum using only one variable.
    """
    largest = None
    for item in items:
        if largest is None or item > largest:
            largest = item
    return largest


def linear_space(n):
    """O(n): Linear extra space—memory grows in proportion to n.
    Example: create a copy of n input values.
    """
    copy = [0] * n
    return copy
