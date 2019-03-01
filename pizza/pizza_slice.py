import factornum as fct
import numpy as np

def read_pizza(filename):
    with open(filename) as f:
        lines = f.readlines()
        R, C, L, H = [int(n) for n in lines[0].split()]
        # Let Tomatoes 'T' be 1 and Mushrooms 'M' be 0
        pizza = np.array([list(map(lambda item: 1 if item == 'T' else 0, row.strip())) for row in lines[1:]])
        
        return R, C, L, H, pizza

def generate_shapes(L, H):
    shapes = []
    for num in range(2*L, H+1):
        factors = fct.factor_tuple(fct.factorint(num))
        for f in factors:
            shapes.append(f)
            shapes.append((f[1], f[0]))
    return set(shapes)

def satisfy_constrain(pizza, shapes, L, r, c):
    for shape in shapes:
        dr = shape[0]
        dc = shape[1]
        pizza_slice = pizza[r:r+dr, c:c+dc]
        tomatoes = np.sum(pizza_slice)
        mushrooms = pizza_slice.size - tomatoes
        if tomatoes >= L and mushrooms >= L:
            print(pizza_slice)
            return shape

if __name__ == '__main__':
    R, C, L, H, pizza = read_pizza('a_example.in')
    shapes = generate_shapes(L, H)
    shape = satisfy_constrain(pizza, shapes, L, 0, 0)
    print(pizza)
    print(shape)