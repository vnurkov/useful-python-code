def squares(x):
    return x*x

def sum_of_squares(x,y):
    return squares(x) + squares(y)

def main(a,b,c):
    if a > c and b > c:
        return sum_of_squares(a,b)
    if a > b and c > b:
        return sum_of_squares(a,c)
    else:
        return sum_of_squares(b,c) 


if __name__ == '__main__':
    print(main(1,2,3))
