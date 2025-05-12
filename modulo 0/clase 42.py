def divide(a:int, b: int) -> float:
    #validar ambos parámetros enteros
    if not isinstance(a,int) or not isinstance (b, int):
        print('Error: ambos parámetros deben ser enteros o flotantes')
        return None

    #verificamos que el divisor no sea cero
    if b ==0:
        print("Error: el divisor no puede ser cero")
        return None
    return a/b

res_1 = divide(10,"2")
res_2 = divide(10,2)
print(res_2)
res_3 =divide(10,0)
