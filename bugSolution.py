def my_function(x):
    if x < 0:
        return 0  # Handle negative input
    elif x == 0:
        return 0
    else:
        return x + my_function(x - 1)

print(my_function(5))
print(my_function(-1)) # Now this will work correctly
print(my_function(1000)) # This will also avoid RecursionError