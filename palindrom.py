def is_palindrom(string: str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def run():
    print(is_palindrom(1000))


if __name__ == '__main__':
    run()
    # En consola usamos
    # mypy palindrome.py --check-untyped-defs


