#################
# PRIME
# Copyright 2015
# License: MIT
# Author: Sam Webb


# IMPORTS
from random import random
from math import ceil


# This is the main checker for prime numbers.
# 
# Example:
# >>> isPrime(5)
# True
# >>> isPrime(6)
# False
#
# @argument num == int: The number you want to check
#
# @returns bool: True if prime, False if nots
#
def isPrime(num):
  # Set original prime variable to True
  prime = True
  # Auto return 2 as prime
  if num == 2:
    return prime
  # Set iterator to 3
  i = 3
  half = num / 2
  if num % 2 == 0:
    prime = False
    return prime

  while i < half and i < 1299:
    if num % i == 0:
      prime = False
      return prime
    i = i + 2
  return prime


# Checks all the numbers including and between
# the start and finish, returning a list of 2
# item lists [[int, bool], [int, bool]]
#
# WARNING: When checking a particularly large range of
# numbers, it is possible that your terminal window will
# crash. For now, try to keep your range low. My Macbook
# Pro terminal, running zsh, crashed with the range
# 3 - 99999999. I have not tried any other big checks yet.
#
# Example:
# >>> check = checkAll(3,6)
# [[3, True], [4, False], [5, True], [6, False]]
#
# @argument start == int: First number to be checked
# @argument finish == int: Counts up to and includes this number
# @argument watch == bool: Shows each number being checked
#
# @return int: The number checked
# @return bool: True if prime, False if not
#
def checkAll(start, finish, watch=False):
  i = start
  checks = []
  while i < (finish + 1):
    checks.append([i, isPrime(i)])
    if watch == True:
      print(str(i) + ": " + str(isPrime(i)))
    i = i + 1
  return checks


# Used to display the return value of checkAll() in an
# easily readable format
#
# @argument check == list: A list returned from checkAll()
#
# @return NO RETURN VALUE
def display(check, primes=False):
  if type(check) == list:
    length = len(check)
    i = 0
    print('-' * 15)
    while i < length:
      if check[i][1] == True:
        print(str(check[i][0]) + ' is a prime number.')
        print('-' * 15)
      else:
        if primes == False:
          print(str(check[i][0]) + ' is not a prime number.')
          print('-' * 15)
      i = i + 1
  else:
    raise TypeError('display() requires a list of lists with an example format of: [[int, bool], [int, bool]]')
  return


# Used to return a large prime number
#
# No arguments
#
# @return int: The large prime number
def bigPrime():
  prime = False
  check = 0
  while prime == False:
    check = int(ceil(random() * 1000000000000000))
    if isPrime(check):
      prime = True
  return check

# Returns a prime number of the specified size
#
# @argument size == int: How large you want the returned prime number
#
# @return int: The prime number
def primeChoice(size=5):
  if type(size) != int:
    raise TypeError('primeChoice() requires an integer for an argument')
  prime = False
  check = 0
  newsize = int('1' + '0' * size)
  check = int(ceil(random() * newsize))
  while prime == False:
    if len(str(check)) == size:
      if isPrime(check):
        prime = True
      else:
        check+=1
    else:
      check = int(ceil(random() * newsize))
  return int(check)

