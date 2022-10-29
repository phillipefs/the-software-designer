
from typing import Callable

#Callable que recebe um int e retorna um int
int_function = Callable[[int], int]
'''
Type Hints tem como objetivo especificar a entrada e saída de dados. 
Funciona apenas como documentação, pois se passar uma str o python irá aceitar.
'''
def add_three(num: int) -> int:
    return num + 3


############################
def main():
    my_var: int_function = add_three
    print(my_var(5))


if __name__ == '__main__':
    main()