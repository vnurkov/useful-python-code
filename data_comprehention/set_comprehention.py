names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]
comprehention = { name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }

if __name__ == "__main__":
    print comprehention