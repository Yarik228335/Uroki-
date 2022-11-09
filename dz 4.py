import random
def shifrator():
    __1 = int(input("Numeric 1: "))
    __2 = int(input("Numeric 2: "))

    for i in range(10):
        op = random.randint(1, 3)
        if op == 1:
            p = __1 + __2
            print(f"Turned in {p}")
        elif op == 2:
            m = __1 - __2
            print(f"Turned in {m}")
        elif op == 3:
            mm = __1 * __2
            print(f"Turned in {mm}")
        elif op == 4:
            d = __1 / __2
            print(f"Turned in {d}")

shifrator()
