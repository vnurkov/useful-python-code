def avg(x,y):
    return (x+y)/2

def square(x):
    return x*x

def improve(guess,x):
    return avg(guess, (x/square(guess) + 2*guess)/3)

def abs(x):
    if x < 0:
        return -x
    else:
        return x

def good_enough(guess,x):
    if abs(square(guess) - x) < 0.01:
        return True
    else:
        return False

def cbrt_iter(guess,x):
    if good_enough(guess,x):
        return guess
    else:
        return cbrt_iter(improve(guess,x),x)

def cbrt(x):
    return cbrt_iter(1.0,x)
