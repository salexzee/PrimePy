#PrimePy

This is just a repository for me to mess around with prime numbers.


##Documentation

It is extremely easy to use PrimePy.

First make sure you import PrimePy:

```python
# To put all PrimePy variables in global scope (dangerous)
from prime import *

# To keep everything namespaced under prime (safe)
import prime
```

----------

**isPrime**

Used to check if a number is prime or not.

Args: (num)

ArgsType: (int)

- @num: The number you want to check.

```python
>>> isPrime(4)
False
>>> isPrime(7)
True
```

----------


**checkAll**

Runs the isPrime method on every number in the specified range. Be careful not to put a range too large or your terminal/application may crash.

Args: (start, finish, [watch])

ArgsType: (int, int, [bool])

- @start: The starting number for your check. (included)
- @finish: The ending number for your checks. (included)
- @watch: Set to true if you'd like to watch the process in the terminal window. Defaults to False.

```python
>>> checkAll(3,5)
[[3, true], [4, false], [5, true]]
```

----------

**display**

Accepts a checkAll formatted list and beautifies it for the terminal.

```python
>>> check = checkAll(3,5)
>>> display(check) # Check output in terminal window
```

----------

**bigPrime**

Returns a large prime number.

```python
>>> bigPrime()
208076533816577
```


##Tests

To run tests, navigate to the `prime` directory in your terminal and execute the following command:

```
$ python tests.py
```