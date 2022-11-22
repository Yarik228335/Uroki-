try:
    result = []
    def divider(a, b):
        if a < b:
            return a+b
        if b > 100:
            raise IndexError
        return a-b
    data = {10: 2, 2: 5, 123: 4, 18: 1, 1: 15, 8 : 4}

    for key in data:
        res = divider(key, data[key])
        result.append(res)
    print(result)
except NameError:
    print("Oh noo, We have a name error:(")
except SyntaxError:
    print("Oh noo, We have a syntax error:(")
except TypeError:
    print("Oh noo,We have a type error:(")




