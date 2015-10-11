#################
# PRIME
# Copyright 2015
# License: MIT
# Author: Sam Webb


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
# 3 - 99999999.
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
    checks.append([i, check_prime(i)])
    if watch == True:
      print(str(i) + ": " + str(check_prime(i)))
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

