mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = { k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys() }

if __name__ == '__main__':
    print mcase_frequency