# Find avarages
def avg(x,y):
    return (x+y)/2

# Improve algo
def improve(guess,x):
    return avg(guess,x/guess)

# Get absolute value of a number
def abs(x):
    if x < 0:
        return -x
    else:
        return x

# Get squares of numbers
def square(x):
    return x*x

# Calculate good enough measure
def good_enough(guess,x):
    if abs(square(guess) - x) < 0.001:
        return True
    else:
        return False

def sqrt_iter(guess,x):
    if good_enough(guess,x):
        return guess
    else:
        return sqrt_iter(improve(guess,x), x)

def sqrt(x):
    return sqrt_iter(1.0,x)


