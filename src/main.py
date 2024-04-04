from funcs import get_main

if __name__ == '__main__':
    # get_main('operations.json')
    for row in get_main('operations.json'):
        print(*row, sep='\n', end='\n\n')
