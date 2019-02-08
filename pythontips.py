# Intermediate Python Tips

# *args and **kwargs
# allow you to pass a variable number of arguments into a function
# *args is used to send a non-keyworded variable length argument list to the function
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('meow', 'dog1', 'dog2', 'dog3')

# **kwargs allows you to pass keyworded variable length of arguments to a function
# You should use **kwargs if you want to handle named arguments in a function
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="michael")
