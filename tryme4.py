import math
# example 1
def python_is_great(var):
    incoming = str(var)
    print(f"Working: {incoming}")
    
    python_is_great()
    python_is_great(var)
    python_is_great("var")  
# example 2
im_a_variable = "I'm a value"

single_result = (math.ceil(9.94))
im_an_expression = single_result

python_is_great("I'm a value")
python_is_great(im_a_variable)
python_is_great(im_an_expression)
# example 3
def local_var_fun(var):
    here_we_go_again = str(var)
    print(f"Variable: {here_we_go_again}")

print(here_we_go_again)
# example 4
def fun_with_arg(unique_name):
    get_the_param = f"{unique_name}You cant get me!"
    print(get_the_param)

print(get_the_param)
# example 5
outside_var = 2 + 2

def new_funk():
    outside_var = 6 + 6
    print(outside_var)

new_funk()

print(outside_var)