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
# Example
def multiply_all_by_numb(numb, *args, text="* DAUGYBA"):
    for elem in args:
        print(f"{elem * numb} {text}")

multiply_all_by_numb(7, 10, 11, 50)
multiply_all_by_numb(7, 10, 11, 50, text="***")
# Example
def return_list_of_multiplied_numbs(numb, *args, info=False):
    multiplied_numbs = [elem * numb for elem in args]
    if info:
        print(f"daugiklis: {numb}, args: {args}, rezultatas: {multiplied_numbs}")
    return multiplied_numbs

res = return_list_of_multiplied_numbs(7, 10, 11, 50)
print(res)  # [70, 77, 350]

res = return_list_of_multiplied_numbs(3, 10, 11, 50, info=True)  # daugiklis yra: 3 *args yra: (10, 11, 50) rezultatas yra: [30, 33, 150]
print(res)  # [30, 33, 150]