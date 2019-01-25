def ex_recursion(x):
    if(x > 0):
        result = x + ex_recursion(x - 1)
        print(result)
    else:
        result = 0
    return result
    
ex_recursion(6)