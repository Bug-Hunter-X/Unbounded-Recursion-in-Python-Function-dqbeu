def my_function(x):
    if x == 0:
        return 0
    else:
        return x + my_function(x - 1)

print(my_function(5)) #This will cause a RecursionError for large values of x
print(my_function(-1)) # This will cause a RecursionError