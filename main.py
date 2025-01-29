# Example
def print_args(*args):
    print(args)
    print(type(args))

print_args("Adomas", "sausis", 1000)
print('-----------------------------------------')
# Example
def give_hello_to_names(*args):
    res = ""
    for name in args:
        res += f"Hello {name}\n"
    return res

print(give_hello_to_names("Ram", "Adomas", "Valdas"))
print('-----------------------------------------')
# Example
def multiply_all_by_numb(numb, *args):
    for elem in args:
        print(elem * numb)

multiply_all_by_numb(7, 10, 11, 50)