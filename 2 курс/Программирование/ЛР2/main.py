"""
Реализовать нерекурсивный вариант функции, позволяющей строить бинарное дерево.
"""
import math
import timeit
import hypothesis.strategies as st

def eval_expression(input_string):
    allowed_names = {
        "sum": sum,
        "pow": pow,
        "sin": math.sin,
        "cos": math.cos,
        "tg": math.tan,
        "sqrt": math.sqrt,
        "lambda": 0,
        "x": 0
    }
    code = compile(input_string, "<string>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"Использование {name} не разрешено.")


def gen_bin_tree_non_rec(height, root, func1, func2):
    tree = {str(root): []}
    if height == 1:
        return tree

    tree = [[0] * 2**(i - 1) for i in range(1, height + 1)]
    tree[0][0] = root

    for i in range(1, height):
        for j in range(0, len(tree[i]), 2):
            k = j // 2
            tree[i][j] = func1(tree[i - 1][k])
            tree[i][j + 1] = func2(tree[i - 1][k] * 2)

    return tree

def main():
    # h = int(input("height = "))
    # r = int(input("root = "))
    # fl = "lambda x: " + str(input("f1(x) = "))
    # fr = "lambda x: " + str(input("f2(x) = "))

    # eval_expression(fl)
    # eval_expression(fr)
    # fl = eval(fl)
    # fr = eval(fr)

    # result = gen_bin_tree_non_rec(h, r, fl, fr)
    # print(result)

    timeRes = timeit.repeat("for x in range(1, 10): gen_bin_tree_non_rec(x, 5, lambda x: x+2, lambda x: x**2)", "from __main__ import gen_bin_tree_non_rec", number=1000)
    print(min(timeRes) * 1000)

   


if __name__ == '__main__':
    main()
