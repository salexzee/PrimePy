#PrimePy

This is just a repository for me to mess around with prime numbers.


##Documentation

It is extremely easy to use PrimePy.

----------

*isPrime*

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


*checkAll*

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


##Tests
```
$ python tests.py
```