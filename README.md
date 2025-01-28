# Unbounded Recursion in Python
This repository demonstrates an example of unbounded recursion in a Python function. The function `my_function` is recursively defined, but lacks a proper base case to handle all possible inputs. This leads to a `RecursionError` when called with certain arguments.

## Bug Description
The `my_function` calculates the sum of numbers from 0 up to the given input `x`. However, it's not correctly handling negative inputs. This means the function will keep calling itself indefinitely until it hits the maximum recursion depth, causing the `RecursionError`. The second `print` statement also demonstrates that negative inputs will cause infinite recursion.

## Solution
The provided solution adds checks to handle negative input and a proper base case to stop recursion when x reaches 0.