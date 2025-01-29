# 1 Task
def sum_all_numbers(*args):
    return sum(args)
print(sum_all_numbers(5, 10, 15))
print(sum_all_numbers(100, 200, 300))
# 2 Task
def sveikinti_vardus(*args):
    res = ""
    for name in args:
        res += f"Hello {name}\n"
    return res
print(sveikinti_vardus("Jonas", "Asta", "Mantas"))
# 3 Task
def pakelti_laipsniu(n, *args):
    for num in args:
        print(n**num)
pakelti_laipsniu(3, 2, 3, 4)
# 4 Task
def spausdinti_zinutes(kartai, *args, pabaiga="!"):
    for zinute in args:
        print((zinute +" ")*kartai+pabaiga)
spausdinti_zinutes(3, "Kaip sekasi", pabaiga="?")
# 5 Task
def dauginti_skaicius(n: int, *args: int):
     return [elem * n for elem in args]
print(dauginti_skaicius(7, 10, 11, 50))




