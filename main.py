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
print('-------------------------------------------------------------------------')
# Example
def print_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
print_kwargs(pirmas=1, antras=2)
# Example
def print_list(listas, skirtukas=" ", eilutes_pabaiga="\n"):
    for elem in listas:
        print(elem, "mėn.", sep=skirtukas, end=eilutes_pabaiga)

listas_duom = ['sausis', 'vasaris', 'kovas']
print_list(listas_duom)
print_list(listas_duom, skirtukas="|||", eilutes_pabaiga="***\n")
print('-------------------------------------------------------------------------')
# Example
def kelk_laipsniu (sk, laipsnis = 2, **kwargs):
    res = sk ** laipsnis
    return res
print(kelk_laipsniu(2, laipsnis=3, radianas=2))
# Example
def call_kelk_lapsniu(sk, **kwargs):
    return kelk_laipsniu(sk, **kwargs)

print('-------------------------------------------------------------------------')
#  Example
darbuotojai = [
    ['Valdas', 'programuotojas', 2000],
    ['Adomas', 'direktorius', 3000],
    ['Aldona', 'vadybininkas', 1800],
    ['Jogaila', 'programuotojas', 2500]
]

# Rūšiavimas pagal pirmąjį elementą (vardą) – numatytoji rūšiavimo tvarka
res = sorted(darbuotojai)
print(res)

# 2
def grazink_index_1(listas):
    return listas[1]  # grąžina profesiją

res = sorted(darbuotojai, key=grazink_index_1)
print(res)
# 3
res = sorted(darbuotojai, key=lambda listas: listas[-1])  # rūšiavimas pagal atlyginimą
print(res)
# 4
def sudeti (a,b):
    return a +b
print(sudeti(3,5))

sudeti_lambda = lambda a, b: a + b
sudeti_lambda(3,5)