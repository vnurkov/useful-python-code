a_list = [1, 5, 'a', 2, 'b']

squared_ints = [e**2 for e in a_list if type(e) is int]


if __name__ == "__main__":
    print squared_ints