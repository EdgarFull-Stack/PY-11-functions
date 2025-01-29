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
        print(num ** n)
pakelti_laipsniu(2, 2, 3, 4)
