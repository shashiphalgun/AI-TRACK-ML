y = 2
eta = 0.01
eps = 0.000001
del_x = 1
max_iters = 1000
iters = 0

def deriv(x):
    x_deriv = 4*(x)*(x)*(x) + 6*(x)
    return x_deriv

while abs(del_x) > eps and iters < max_iters:
    prev_x = y
    del_x = -eta * deriv(prev_x)
    y = y + del_x
    iters = iters +1
    print("Iteration",iters,"\nx value is",y)
    
print("the local minimum occurs at",y)