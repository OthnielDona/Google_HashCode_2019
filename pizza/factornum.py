def factorint(num):
    factors = []
    num = int(num)
    
    for n in range(1, num+1):
        if not (num % n):
            factors.append(n)
            if num/n == n: factors.append(n)
    
    return factors

def factor_tuple(factors_list):
    factors = []
    while len(factors_list) > 0:
        factors.append((factors_list.pop(0), factors_list.pop()))
    return factors
    
if __name__ == '__main__':
    import sys
    num = sys.argv[1]
    print(factorint(num), factor_tuple(factorint(num)), sep='\n')
    
