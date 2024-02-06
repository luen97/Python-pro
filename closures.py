from typing import Callable

def make_repeater_of(n):
    def repeater(string):
        assert type(string) ==  str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater

# Usamos Callable cuando queremos indicar que una función 
# devolverá a otra función.
# Callable recibe dos valores: la lista de argumentos 
# y el tipo de retorno. La lista de argumentos debe ser
# una lista de tipos o puntos suspensivos; el tipo de
# retorno debe ser un solo tipo.
# https://docs.python.org/3/library/typing.html#typing.Callable

def make_division_by(n: float) -> Callable[[float], float]:
    def divide(x: float) -> float:
        return x/n

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('hola'))
    repeat_10 = make_repeater_of(10)
    print(repeat_10('buneas'))

if __name__ == '__main__':
    run()




