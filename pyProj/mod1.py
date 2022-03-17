def func1(a, b):
    x = a
    y = b

    def func2():
        nonlocal x, y
        return f"Для значений {x}, {y} функция f({x},{y}) = {x + y}"
    return func2
