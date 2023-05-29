"""
Построение бинарного дерева
"""
import json
import math
import timeit

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


def gen_bin_tree(height, root, f1, f2):
    tree = {str(root): []}

    if height == 1:
        return tree

    left_leaf = f1(root)
    right_leaf = f2(root)

    height -= 1
    tree[str(root)] = [
        gen_bin_tree(height, left_leaf, f1, f2),
        gen_bin_tree(height, right_leaf, f1, f2)
    ]
    return tree


def main():
    # h = int(input("height = "))
    # r = int(input("root = "))
    # fl = "lambda x: " + str(input("f1(x) = "))
    # fr = "lambda x: " + str(input("f2(x) = "))

    # eval_expression(fl)
    # eval_expression(fr)
    #fl = eval(fl)
   # fr = eval(fr)

   # result = gen_bin_tree(h, r, fl, fr)

    timeRes = timeit.repeat("for x in range(1, 10): gen_bin_tree(x, 5, lambda x: x+2, lambda x: x**2)", "from __main__ import gen_bin_tree", number=1000)
    print(min(timeRes) * 1000)

    # print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
